import express from "express";

const app = express();
const port = Number(process.env.PORT ?? 5000);

app.get("/", (_req, res) => {
  res.send("API running");
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Express API listening on port ${port}`);
});
