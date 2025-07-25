document.addEventListener('DOMContentLoaded', function() {
    // 獲取 DOM 元素
    const openSidebarBtn = document.getElementById('open');
    const closeSidebarBtn = document.querySelector('.close-btn');
    const sidebarMenu = document.querySelector('.sidebar-menu');
    const overlay = document.querySelector('.overlay');

    // 監聽漢堡圖示點擊事件 (打開菜單)
    if (openSidebarBtn) {
        openSidebarBtn.addEventListener('click', function() {
            sidebarMenu.classList.add('active'); // 為菜單添加 active class
            overlay.classList.add('active');     // 為遮罩添加 active class
        });
    }

    // 監聽關閉按鈕點擊事件 (關閉菜單)
    if (closeSidebarBtn) {
        closeSidebarBtn.addEventListener('click', function() {
            sidebarMenu.classList.remove('active'); // 移除 active class
            overlay.classList.remove('active');     // 移除 active class
        });
    }

    // 監聽遮罩層點擊事件 (點擊遮罩也可關閉菜單)
    if (overlay) {
        overlay.addEventListener('click', function() {
            sidebarMenu.classList.remove('active'); // 移除 active class
            overlay.classList.remove('active');     // 移除 active class
        });
    }

    // 監聽菜單項目點擊事件 (點擊菜單選項後關閉菜單，可選)
    const menuItems = document.querySelectorAll('.menu-list a');
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            // 您可以根據需要決定點擊後是否自動關閉菜單
            // sidebarMenu.classList.remove('active');
            // overlay.classList.remove('active');
        });
    });
});