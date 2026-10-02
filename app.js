async function apiPost(url, body) {
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': CSRF_TOKEN,
    },
    body: JSON.stringify(body || {}),
  });
  return res.json();
}

async function addToCart(id) {
  const data = await apiPost(ENDPOINTS.add, { product_id: id });
  renderCart(data);
  showToast('Added to crate');
}

async function checkout() {
  const res = await fetch(ENDPOINTS.checkout, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': CSRF_TOKEN },
    body: JSON.stringify({}),
  });
  const data = await res.json();
  if (res.ok) {
    showToast(`Order #${data.order_id} placed — $${data.total.toFixed(2)}`);
  }
}
