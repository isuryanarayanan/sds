export default {
  pushToEvents: function(state, arg) {
    state.events.push(arg);
  },
  deleteFromEvents: function(state, arg) {
    for (var i = 0; i < state.events.length; i++) {
      if (state.events[i].id === arg) {
        state.events.splice(i, 1);
      }
    }
  },
  set_today: function(state) {
    state.focus = "";
    state.type = "week";
  },
  set_type: function(state, arg) {
    state.type = arg;
  },
  set_focus: function(state, arg) {
    state.focus = arg;
  },
  set_ready: function(state, arg) {
    state.ready = arg;
  },
  set_selectedEvent: function(state, arg) {
    state.selectedEvent = arg;
  },
  set_selectedElement: function(state, arg) {
    state.selectedElement = arg;
  },
  set_selectedOpen: function(state, arg) {
    state.selectedOpen = arg;
  },
  set_dragEvent: function(state, arg) {
    state.dragEvent = arg;
  },
  set_dragStart: function(state, arg) {
    state.dragStart = arg;
  },
  set_dragTime: function(state, arg) {
    state.dragTime = arg;
  },
  set_createEvent: function(state, arg) {
    state.createEvent = arg;
  },
  set_createStart: function(state, arg) {
    state.createStart = arg;
  },
  set_extendOriginal: function(state, arg) {
    state.extendOriginal = arg;
  },
  set_refs: function(state, arg) {
    state.refs = arg;
  },
};
