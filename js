document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const videoId = new URL(window.location.href).searchParams.get("v");
  if (!videoId) return;

  const response = await fetch(`http://localhost:5000/summarize/${videoId}`);
  const data = await response.json();
  document.getElementById("summary").innerText = data.summary;
});
