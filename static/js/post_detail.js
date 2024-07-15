document.addEventListener('DOMContentLoaded', function() {
    // تغییر تصویر اصلی با کلیک روی تصاویر کوچک
    const mainImage = document.getElementById('main-image');
    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            mainImage.src = this.src;
        });
    });

    // افزودن به سبد خرید
    const addToCartButton = document.getElementById('add-to-cart');
    addToCartButton.addEventListener('click', function() {
        alert('محصول به سبد خرید اضافه شد!');
        // اینجا می‌توانید کد مربوط به اضافه کردن محصول به سبد خرید را قرار دهید
    });

    // نمایش اطلاعات محصول (در یک سناریوی واقعی، این اطلاعات از سرور دریافت می‌شوند)
    const productName = document.getElementById('product-name');
    const productPrice = document.getElementById('product-price');
    const productAvailability = document.getElementById('product-availability');

    // مثال: دریافت اطلاعات محصول از یک API
    fetch('https://api.example.com/product/1')
        .then(response => response.json())
        .then(data => {
            productName.textContent = data.name;
            productPrice.innerHTML = `قیمت: <span>${data.price}</span> تومان`;
            productAvailability.innerHTML = `موجودی: <span>${data.inStock ? 'در انبار' : 'ناموجود'}</span>`;
        })
        .catch(error => console.error('Error:', error));

    // مدیریت تعداد محصول
    const decreaseQuantityButton = document.getElementById('decrease-quantity');
    const increaseQuantityButton = document.getElementById('increase-quantity');
    const productQuantityInput = document.getElementById('product-quantity');

    decreaseQuantityButton.addEventListener('click', function() {
        let currentQuantity = parseInt(productQuantityInput.value);
        if (currentQuantity > 1) {
            productQuantityInput.value = currentQuantity - 1;
        }
    });

    increaseQuantityButton.addEventListener('click', function() {
        let currentQuantity = parseInt(productQuantityInput.value);
        productQuantityInput.value = currentQuantity + 1;
    });
});