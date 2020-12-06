<template>
  <v-row class="">
    <v-col>
      <v-sheet><toolbar @prev="prev" @next="next"></toolbar></v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :type="type"
          :events="events"
          :event-color="getEventColor"
          :event-ripple="false"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
          @mousedown:event="startDrag"
          @mousedown:time="startTime"
          @mousemove:time="mouseMove"
          @mouseup:time="endDrag"
          @mouseleave.native="cancelDrag"
        >
          <template v-slot:event="{ event, timed, eventSummary }">
            <div class="v-event-draggable" v-html="eventSummary()"></div>
            <div
              v-if="timed"
              class="v-event-drag-bottom"
              @mousedown.stop="extendBottom(event)"
            ></div>
          </template>
          <template v-slot:day-body="{ date, week }">
            <div
              class="v-current-time"
              :class="{ first: date === week[0].date }"
              :style="{ top: nowY }"
            ></div>
          </template>
        </v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <eventCardComponent />
        </v-menu>
      </v-sheet>
    </v-col>
  </v-row>
</template>
<script>
import { mapGetters } from "vuex";
import eventCardComponent from "./eventComponent.vue";
import toolbar from "./toolbarComponent.vue";
export default {
  components: {
    toolbar,
    eventCardComponent,
  },
  computed: {
    focus: {
      get() {
        return this.$store.getters["get_focus"];
      },
      set(arg) {
        this.$store.commit("set_focus", arg);
      },
    },
    selectedOpen: {
      get() {
        return this.$store.getters["get_selectedOpen"];
      },
      set(arg) {
        this.$store.commit("set_selectedOpen", arg);
      },
    },
    ...mapGetters({
      getGlobal: "get_global",
      value: "get_value",
      events: "get_events",
      type: "get_type",
      ready: "get_ready",
      typeToLabel: "get_typeToLabel",
      colors: "get_colors",
      names: "get_names",
      selectedEvent: "get_selectedEvent",
      selectedElement: "get_selectedElement",
      selectedOpen: "get_selectedOpen",
      dragEvent: "get_dragEvent",
      dragStart: "get_dragStart",
      dragTime: "get_dragTime",
      createEvent: "get_createEvent",
      createStart: "get_createStart",
      extendOriginal: "get_extendOriginal",
    }),
    cal() {
      return this.ready ? this.$refs.calendar : null;
    },
    nowY() {
      return this.cal ? this.cal.timeToY(this.cal.times.now) + "px" : "-10px";
    },
  },
  mounted() {
    this.$store.commit("set_refs", this.$refs);
    this.$store.commit("set_ready", true);
    this.scrollToTime();
    this.updateTime();
  },
  methods: {
    getCurrentTime() {
      return this.cal
        ? this.cal.times.now.hour * 60 + this.cal.times.now.minute
        : 0;
    },
    scrollToTime() {
      const time = this.getCurrentTime();
      const first = Math.max(0, time - (time % 30) - 30);

      this.cal.scrollToTime(first);
    },
    updateTime() {
      setInterval(() => this.cal.updateTimes(), 60 * 1000);
    },
    viewDay({ date }) {
      this.$store.commit("set_focus", date);
      this.$store.commit("set_type", "day");
    },

    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },

    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.$store.commit("set_selectedEvent", event);
        this.$store.commit("set_selectedElement", nativeEvent.target);

        setTimeout(() => {
          this.$store.commit("set_selectedOpen", true);
        }, 10);
      };

      if (this.selectedOpen) {
        this.$store.commit("set_selectedOpen", false);
        setTimeout(open, 10);
      } else {
        open();
      }
      nativeEvent.stopPropagation();
    },
    startDrag({ event, timed }) {
      if (event && timed) {
        this.$store.commit("set_dragEvent", event);
        this.$store.commit("set_dragTime", null);
        this.$store.commit("set_extendOriginal", null);
      }
    },
    startTime(tms) {
      const mouse = this.toTime(tms);

      if (this.dragEvent && this.dragTime === null) {
        const start = this.dragEvent.start;
        this.$store.commit("set_dragTime", mouse - start);
      } else {
        this.$store.commit("set_createStart", this.roundTime(mouse));
        this.$store.commit("set_createEvent", {
          id: this.events.length,
          name: `Event #${this.events.length}`,
          details: `Event #${this.events.length} details.`,
          color: this.rndElement(this.colors),
          start: this.createStart,
          end: this.createStart,
          timed: true,
        });
        this.$store.commit("pushToEvents", this.createEvent);
      }
    },
    extendBottom(event) {
      this.$store.commit("set_createEvent", event);
      this.$store.commit("set_createStart", event.start);
      this.$store.commit("set_extendOriginal", event.end);
    },
    mouseMove(tms) {
      const mouse = this.toTime(tms);

      if (this.dragEvent && this.dragTime !== null) {
        const start = this.dragEvent.start;
        const end = this.dragEvent.end;
        const duration = end - start;
        const newStartTime = mouse - this.dragTime;
        const newStart = this.roundTime(newStartTime);
        const newEnd = newStart + duration;

        console.log(this.dragTime);
        this.dragEvent.start = newStart;
        this.dragEvent.end = newEnd;

        this.$store.commit("set_dragEvent", this.dragEvent);
      } else if (this.createEvent && this.createStart !== null) {
        const mouseRounded = this.roundTime(mouse, false);
        const min = Math.min(mouseRounded, this.createStart);
        const max = Math.max(mouseRounded, this.createStart);

        this.createEvent.start = min;
        this.createEvent.end = max;
        this.$store.commit("set_createEvent", this.createEvent);
      }
    },
    endDrag() {
      this.$store.commit("set_dragTime", null);
      this.$store.commit("set_dragEvent", null);
      this.$store.commit("set_createEvent", null);
      this.$store.commit("set_createStart", null);
      this.$store.commit("set_extendOriginal", null);
    },
    cancelDrag() {
      if (this.createEvent) {
        if (this.extendOriginal) {
          this.$store.commit("set_createEvent", this.extendOriginal);
        } else {
          const i = this.events.indexOf(this.createEvent);
          if (i !== -1) {
            this.events.splice(i, 1);
          }
        }
      }

      this.$store.commit("set_dragTime", null);
      this.$store.commit("set_dragEvent", null);
      this.$store.commit("set_createEvent", null);
      this.$store.commit("set_createStart", null);
    },
    roundTime(time, down = true) {
      const roundTo = 15;
      const roundDownTime = roundTo * 60 * 1000;

      return down
        ? time - (time % roundDownTime)
        : time + (roundDownTime - (time % roundDownTime));
    },
    toTime(tms) {
      return new Date(
        tms.year,
        tms.month - 1,
        tms.day,
        tms.hour,
        tms.minute
      ).getTime();
    },
    getEventColor(event) {
      const rgb = parseInt(event.color.substring(1), 16);
      const r = (rgb >> 16) & 0xff;
      const g = (rgb >> 8) & 0xff;
      const b = (rgb >> 0) & 0xff;

      return event === this.dragEvent
        ? `rgba(${r}, ${g}, ${b}, 0.7)`
        : event === this.createEvent
        ? `rgba(${r}, ${g}, ${b}, 0.7)`
        : event.color;
    },

    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
    rndElement(arr) {
      return arr[this.rnd(0, arr.length - 1)];
    },
  },
};
</script>

<style scoped lang="scss">
.v-event-draggable {
  padding-left: 6px;
}

.v-event-timed {
  user-select: none;
  -webkit-user-select: none;
}

.v-event-drag-bottom {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 4px;
  height: 4px;
  cursor: ns-resize;

  &::after {
    display: none;
    position: absolute;
    left: 50%;
    height: 4px;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
    width: 16px;
    margin-left: -8px;
    opacity: 0.8;
    content: "";
  }

  &:hover::after {
    display: block;
  }
}
.v-current-time {
  height: 2px;
  background-color: #000;
  position: absolute;
  left: -1px;
  right: 0;
  pointer-events: none;

  &.first::before {
    content: "";
    position: absolute;
    background-color: #333;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-top: -5px;
    margin-left: -6.5px;
  }
}
</style>
