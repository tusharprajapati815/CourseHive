document.addEventListener("DOMContentLoaded", function () {
  const totalAmount = parseFloat(document.getElementById("hidden-total").value);

  const formattedTotal = new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
  }).format(totalAmount);

  const totalBillElement = document.getElementById("totalBill");
  if (totalBillElement) {
    totalBillElement.textContent = formattedTotal;
  }
});
