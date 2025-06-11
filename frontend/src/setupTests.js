// src/setupTests.js
import '@testing-library/jest-dom';
// stub out alert() so your Preferences tests won’t blow up
global.alert = () => {};
