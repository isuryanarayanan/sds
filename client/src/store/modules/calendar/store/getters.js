export default {
  get_global: function(state) {
    return state;
  },
  get_value: function(state) {
    return state.value;
  },
  get_events: function(state) {
    return state.events;
  },
  get_focus: function(state) {
    return state.focus;
  },
  get_type: function(state) {
    return state.type;
  },
  get_ready: function(state) {
    return state.ready;
  },
  get_typeToLabel: function(state) {
    return state.typeToLabel[state.type];
  },
  get_colors: function(state) {
    return state.colors;
  },
  get_names: function(state) {
    return state.names;
  },
  get_selectedEvent: function(state) {
    return state.selectedEvent;
  },
  get_selectedElement: function(state) {
    return state.selectedElement;
  },
  get_selectedOpen: function(state) {
    return state.selectedOpen;
  },
  get_dragEvent: function(state) {
    return state.dragEvent;
  },
  get_dragStart: function(state) {
    return state.dragStart;
  },
  get_dragTime: function(state) {
    return state.dragTime;
  },
  get_createEvent: function(state) {
    return state.createEvent;
  },
  get_createStart: function(state) {
    return state.createStart;
  },
  get_extendOriginal: function(state) {
    return state.extendOriginal;
  },
  get_refs: function(state) {
    return state.refs;
  },
};
