// اجرای AOS
AOS.init({
    duration: 1000,
    once: true
});

// اضافه کردن اخبار مرتبط به صورت داینامیک
function addRelatedNews() {
    const relatedNews = [
        { title: "خبر مرتبط اول", image: "news1.jpg" },
        { title: "خبر مرتبط دوم", image: "news2.jpg" },
        { title: "خبر مرتبط سوم", image: "news3.jpg" },
        { title: "خبر مرتبط چهارم", image: "news4.jpg" }
    ];
    const carousel = document.getElementById('related-news-carousel');
    relatedNews.forEach(news => {
        const item = document.createElement('div');
        item.className = 'carousel-item';
        item.innerHTML = `
            <img src="${news.image}" alt="${news.title}" style="width:100%; height:150px; object-fit:cover; border-radius:5px;">
            <h3>${news.title}</h3>
        `;
        carousel.appendChild(item);
    });
}

// اشتراک‌گذاری خبر
function shareNews(platform) {
    const title = document.getElementById('news-title').textContent;
    const url = window.location.href;
    let shareUrl;

    switch(platform) {
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}`;
            break;
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
            break;
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`;
            break;
    }

    window.open(shareUrl, '_blank');
}

// اضافه کردن نظر جدید
document.getElementById('comment-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const commentText = document.getElementById('comment-text').value;
    if (commentText.trim() !== '') {
        const commentElement = document.createElement('div');
        commentElement.className = 'comment fade-in';
        commentElement.textContent = commentText;
        document.getElementById('comments-list').prepend(commentElement);
        document.getElementById('comment-text').value = '';
    }
});

// اجرای توابع هنگام بارگذاری صفحه
window.onload = function() {
    addRelatedNews();
};

// افکت پارالاکس برای هدر
window.addEventListener('scroll', function() {
    const scrollPosition = window.pageYOffset;
    document.querySelector('.hero').style.backgroundPositionY = scrollPosition * 0.5 + 'px';
});