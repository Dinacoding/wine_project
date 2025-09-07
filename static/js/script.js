function constrainBodyHeight() {
    const footer = document.querySelector('footer');
    const body = document.body;
    
    if (footer) {
        const footerTop = footer.offsetTop;
        const footerHeight = footer.offsetHeight;
        const maxBodyHeight = footerTop + footerHeight;
        
        body.style.maxHeight = maxBodyHeight + 'px';
        body.style.overflow = 'hidden';
    }
}