function initiateUPIPayment() {
  const upiId = "745483518566@ibl";
  const name = "PhonePe";  // Optional display name
  const amount = "99";
  const currency = "INR";

  const upiLink = `upi://pay?pa=${upiId}&pn=${name}&cu=${currency}&am=${amount}`;

  // Redirect to UPI payment app
  window.location.href = upiLink;

  // Optional: show fake success message after delay
  setTimeout(() => {
    alert("Payment Successful! Thank you for registering.");
    // You can also redirect to a thank-you page here
  }, 5000); // 5 sec delay
}
