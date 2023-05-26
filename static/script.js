function updateClock() {
  var now = new Date();
  document.getElementById("clock").textContent = now.toLocaleTimeString();
}

// Call the updateClock function every second
setInterval(updateClock, 1000);

// Define a function to handle login button click
function handleLogin() {
  // Redirect the user to the home page
  window.location.href = "index.html";
}

// Add an event listener to the login button
document.getElementById("loginButton").addEventListener("click", handleLogin);
