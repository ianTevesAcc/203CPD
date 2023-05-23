function updateClock() {
  var now = new Date();
  document.getElementById("clock").textContent = now.toLocaleTimeString();

}

// Call the updateClock function every second
setInterval(updateClock, 1000);
