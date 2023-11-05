let sessionTimeout;
const sessionTimeoutDuration = 30000; // 1 minute in milliseconds

function resetSessionTimeout() {
  clearTimeout(sessionTimeout);
  sessionTimeout = setTimeout(logoutUser, sessionTimeoutDuration);
}

function logoutUser() {
  // Perform the logout or session invalidation action here
  alert("Your session has timed out. Please log in again.");
  // Redirect the user to the login page or perform the desired action
}

// Start the timer when the user logs in or performs an activity
resetSessionTimeout();

// Reset the timer on user activity
document.addEventListener("click", resetSessionTimeout);
document.addEventListener("keydown", resetSessionTimeout);
// Add more event listeners for other user activities as needed
