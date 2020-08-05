export default () => ({
  authenticated: false,
  authorized: false,
  user: {
    mode: 0, // unauthorized and unauthenticated
    id: null,
    username: null,
    email: null,
  },
});
