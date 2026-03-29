import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS Adds
css_to_add = """
        /* ─── NEW FEATURES CSS ─── */
        [data-theme="light"] {
            --bg: #FAF7F2;
            --surface: #FFFFFF;
            --surface2: #f2efe9;
            --primary: #6B1E2E;
            --primary-light: #8f2a3f;
            --primary-dark: #4d1521;
            --text: #1A1A1A;
            --muted: #666666;
            --border: rgba(107, 30, 46, 0.15);
            --border2: rgba(0, 0, 0, 0.08);
            --overlay: rgba(255, 255, 255, 0.9);
        }

        .promo-banner {
            background: var(--primary);
            color: var(--bg);
            height: 40px;
            display: flex;
            align-items: center;
            overflow: hidden;
            position: relative;
            z-index: 60;
            font-size: 0.85rem;
            font-weight: 600;
            transition: height 0.3s;
        }

        .promo-banner.closed {
            height: 0;
            opacity: 0;
            pointer-events: none;
        }

        .marquee-content {
            display: flex;
            white-space: nowrap;
            animation: marquee 25s linear infinite;
        }

        .marquee-content:hover {
            animation-play-state: paused;
        }

        .marquee-item {
            padding: 0 3rem;
        }

        .promo-close {
            position: absolute;
            right: 15px;
            background: rgba(0,0,0,0.1);
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--bg);
            z-index: 2;
            transition: background 0.2s;
        }
        .promo-close:hover { background: rgba(0,0,0,0.3); }

        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        /* Nav additions */
        .search-container {
            position: relative;
            display: none;
            width: 250px;
        }
        @media(min-width: 900px) { .search-container { display: block; } }
        
        .search-input {
            width: 100%;
            background: var(--surface2);
            border: 1px solid var(--border2);
            color: var(--text);
            padding: 0.5rem 1rem 0.5rem 2.5rem;
            border-radius: 2rem;
            font-family: inherit;
            font-size: 0.85rem;
            transition: border-color 0.2s;
        }
        .search-input:focus { border-color: var(--primary); outline: none; }
        .search-icon {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted);
            font-size: 1.1rem !important;
        }
        .theme-toggle {
            background: var(--surface);
            border: 1px solid var(--border);
            width: 36px;
            height: 36px;
            border-radius: 50%;
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.4s;
            cursor: pointer;
        }
        .theme-toggle:hover { background: var(--surface2); transform: scale(1.05); }

        /* Card Image Updates */
        .card-img {
            position: relative;
        }
        .card-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            inset: 0;
            z-index: 1;
            transition: transform 0.4s;
        }
        .card:hover .card-img img {
            transform: scale(1.05);
        }
        .card-img-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60%;
            background: linear-gradient(to top, var(--surface) 0%, transparent 100%);
            z-index: 2;
            pointer-events: none;
        }
        .card-img-fallback {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4.5rem;
            background: linear-gradient(145deg, #1e1c1a, #111);
            z-index: 0;
        }
        [data-theme="light"] .card-img-fallback { background: linear-gradient(145deg, #f0ede6, #e6e2da); }
        .card-stock {
            position: absolute;
            top: 0.8rem;
            right: 0.8rem;
            padding: 0.2rem 0.6rem;
            border-radius: 2rem;
            font-size: 0.65rem;
            font-weight: 800;
            z-index: 3;
            letter-spacing: 0.05em;
        }
        .stock-ok { background: #22c55e; color: #fff; }
        .stock-low { background: #f59e0b; color: #fff; animation: pulse 1.5s infinite; }
        .stock-out { background: #ef4444; color: #fff; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
        
        .card-chip { z-index: 3; }

        .no-results {
            grid-column: 1 / -1;
            text-align: center;
            padding: 4rem 2rem;
            color: var(--muted);
            font-size: 1.1rem;
        }

        /* Reviews Carousel */
        .reviews-section {
            padding: 4rem 0;
            text-align: center;
            overflow: hidden;
            position: relative;
        }
        .carousel-track {
            display: flex;
            transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            width: 100%;
        }
        .review-card {
            min-width: 100%;
            padding: 0 1rem;
            opacity: 0.5;
            transition: opacity 0.5s;
        }
        .review-card.active { opacity: 1; }
        @media(min-width: 768px){
            .review-card { min-width: 50%; }
        }
        @media(min-width: 1024px){
            .review-card { min-width: 33.333%; }
        }
        .review-inner {
            background: var(--surface);
            border: 1px solid var(--border2);
            border-radius: var(--radius-sm);
            padding: 2.5rem 2rem;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
        }
        .review-quote {
            color: var(--primary);
            font-size: 3rem;
            position: absolute;
            top: 10px;
            left: 20px;
            opacity: 0.2;
            font-family: 'Cormorant Garamond', serif;
        }
        .review-text {
            color: var(--text);
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            font-style: italic;
            flex: 1;
        }
        .review-stars { color: var(--primary); margin-bottom: 1rem; letter-spacing: 2px; }
        .review-author { display: flex; align-items: center; gap: 1rem; }
        .review-avatar {
            width: 44px; height: 44px; border-radius: 50%;
            background: var(--primary-dark); color: var(--surface);
            display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 1.1rem;
        }
        .review-name { font-weight: 700; font-size: 0.9rem; text-align: left; }
        .review-date { font-size: 0.75rem; color: var(--muted); }
        .carousel-nav {
            display: flex; justify-content: center; gap: 1rem; margin-top: 2rem;
        }
        .c-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--surface2); transition: 0.3s; cursor: pointer; }
        .c-dot.active { background: var(--primary); transform: scale(1.2); }

        /* IG Gallery */
        .gallery-section { padding: 4rem 2rem 5rem; max-width: 1400px; margin: 0 auto; }
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        @media(min-width: 768px) { .gallery-grid { grid-template-columns: repeat(3, 1fr); } }
        
        .ig-item {
            position: relative;
            padding-bottom: 100%;
            overflow: hidden;
            border-radius: var(--radius-sm);
            cursor: pointer;
        }
        .ig-item img {
            position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
            transition: transform 0.5s;
        }
        .ig-item:hover img { transform: scale(1.08); }
        .ig-overlay {
            position: absolute; inset: 0; background: rgba(0,0,0,0.5);
            display: flex; align-items: center; justify-content: center;
            opacity: 0; transition: opacity 0.3s;
            color: #fff; font-size: 2rem;
        }
        .ig-item:hover .ig-overlay { opacity: 1; }

        /* Lightbox */
        .lightbox {
            position: fixed; inset: 0; background: rgba(0,0,0,0.95);
            z-index: 9999; display: flex; align-items: center; justify-content: center;
            opacity: 0; visibility: hidden; transition: all 0.3s;
        }
        .lightbox.active { opacity: 1; visibility: visible; }
        .lb-content { position: relative; max-width: 90vw; max-height: 90vh; }
        .lb-img {
            max-width: 100%; max-height: 90vh; border-radius: 4px;
            transform: scale(0.9); transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.2);
        }
        .lightbox.active .lb-img { transform: scale(1); }
        .lb-close { position: absolute; top: -40px; right: 0; color: #fff; font-size: 2rem; border:none; background:none; cursor:pointer;}
        .lb-prev, .lb-next {
            position: absolute; top: 50%; transform: translateY(-50%);
            color: #fff; font-size: 3rem; opacity: 0.6; transition: 0.2s; border:none; background:none; cursor:pointer;
        }
        .lb-prev:hover, .lb-next:hover { opacity: 1; }
        .lb-prev { left: -60px; }
        .lb-next { right: -60px; }
        @media(max-width: 768px) {
            .lb-prev { left: 10px; } .lb-next { right: 10px; }
            .lb-close { top: -40px; right: 10px; }
        }

        /* Scroll Animations */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1);
            will-change: opacity, transform;
        }
        .reveal.active { opacity: 1; transform: translateY(0); }
        .reveal-left { opacity: 0; transform: translateX(-50px); transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1); will-change: opacity, transform; }
        .reveal-left.active { opacity: 1; transform: translateX(0); }
        .reveal-right { opacity: 0; transform: translateX(50px); transition: all 0.8s cubic-bezier(0.25, 1, 0.5, 1); will-change: opacity, transform; }
        .reveal-right.active { opacity: 1; transform: translateX(0); }
</style>"""

html = html.replace('</style>', css_to_add)

# 2. Promo Banner + Navbar updates
banner_html = """<body>
    <!-- ═══ PROMO BANNER ═══ -->
    <div class="promo-banner" id="promo-banner">
        <div class="marquee-content">
            <span class="marquee-item">🎂 Tortas personalizadas — pedidos con 48h de anticipación</span>
            <span class="marquee-item">🥟 Docena de empanadas a $12.000</span>
            <span class="marquee-item">🍔 Hamburguesas artesanales con papas incluidas</span>
            <span class="marquee-item">🥂 Banquetería y chef particular para tu evento — cotiza por WhatsApp</span>
            <span class="marquee-item">🎉 Envíos en Valdivia — consulta cobertura</span>
            <!-- duplicate for smooth loop -->
            <span class="marquee-item">🎂 Tortas personalizadas — pedidos con 48h de anticipación</span>
            <span class="marquee-item">🥟 Docena de empanadas a $12.000</span>
            <span class="marquee-item">🍔 Hamburguesas artesanales con papas incluidas</span>
            <span class="marquee-item">🥂 Banquetería y chef particular para tu evento — cotiza por WhatsApp</span>
            <span class="marquee-item">🎉 Envíos en Valdivia — consulta cobertura</span>
        </div>
        <button class="promo-close" aria-label="Cerrar promo" onclick="closePromo()">
            <span class="material-symbols-outlined" style="font-size: 1rem;">close</span>
        </button>
    </div>"""

html = html.replace('<body>', banner_html)

# Navbar updates (Search + Theme toggle)
nav_right_old = """<div class="nav-right">
            <a href="https://wa.me/56992590000" target="_blank" class="nav-wsp">"""
nav_right_new = """<div class="search-container">
            <span class="material-symbols-outlined search-icon">search</span>
            <input type="text" class="search-input" id="search-input" placeholder="Buscar productos..." oninput="handleSearch()">
        </div>
        <div class="nav-right">
            <button class="theme-toggle" id="theme-toggle" onclick="toggleTheme()" aria-label="Cambiar tema">
                <span class="material-symbols-outlined" id="theme-icon">light_mode</span>
            </button>
            <a href="https://wa.me/56992590000" target="_blank" class="nav-wsp">"""

html = html.replace(nav_right_old, nav_right_new)

# Mobile filter tweaks layout
mobile_filters_old = """<div class="mobile-filters" id="mobile-filter-tabs">"""
mobile_filters_new = """
    <div style="padding: 10px 1rem 0; background: var(--bg); display: none;" id="mobile-search">
        <div class="search-container" style="display: block; width: 100%;">
            <span class="material-symbols-outlined search-icon">search</span>
            <input type="text" class="search-input" id="search-input-mobile" placeholder="Buscar productos..." oninput="handleSearchMobile()">
        </div>
    </div>
    <div class="mobile-filters" id="mobile-filter-tabs">"""
html = html.replace(mobile_filters_old, mobile_filters_new)

media_old = """@media(max-width:480px) {
            .mobile-filters {
                display: flex;
            }
        }"""
media_new = """@media(max-width:480px) {
            .mobile-filters { display: flex; }
            #mobile-search { display: block !important; }
        }"""
html = html.replace(media_old, media_new)

# 3. Reviews & Gallery HTML insertions right before footer
reviews_gallery_html = """
    <!-- ═══ REVIEWS ═══ -->
    <section class="reviews-section reveal">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 1rem; position: relative;">
            <p class="section-label" style="justify-content: center; margin-bottom: 3rem;">Lo que dicen nuestros clientes</p>
            <div style="overflow: hidden; padding-bottom:1rem;">
                <div class="carousel-track" id="reviews-track">
                    <!-- Rev 1 -->
                    <div class="review-card active">
                        <div class="review-inner">
                            <span class="review-quote">"</span>
                            <div class="review-stars">★★★★★</div>
                            <p class="review-text">La torta Red Velvet de Lefránfood fue el centro de atención en mi cumpleaños. ¡Absolutamente deliciosa y la decoración impecable! Además el despacho llegó a la hora acordada.</p>
                            <div class="review-author">
                                <div class="review-avatar">CD</div>
                                <div>
                                    <div class="review-name">Camila Díaz</div>
                                    <div class="review-date">Hace 1 semana</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Rev 2 -->
                    <div class="review-card">
                        <div class="review-inner">
                            <span class="review-quote">"</span>
                            <div class="review-stars">★★★★★</div>
                            <p class="review-text">Contratamos el servicio de banquetería corporativa y quedamos fascinados. La presentación de la comida fue de primer nivel y el equipo muy profesional. Recomendados al 100% en Valdivia.</p>
                            <div class="review-author">
                                <div class="review-avatar">JS</div>
                                <div>
                                    <div class="review-name">Javiera Silva</div>
                                    <div class="review-date">Hace 2 semanas</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Rev 3 -->
                    <div class="review-card">
                        <div class="review-inner">
                            <span class="review-quote">"</span>
                            <div class="review-stars">★★★★★</div>
                            <p class="review-text">Las empanadas de pino son literalmente las mejores que he probado en la región. Mucho pino, excelente masa y excelente atención al cliente.</p>
                            <div class="review-author">
                                <div class="review-avatar">PM</div>
                                <div>
                                    <div class="review-name">Pedro Muñoz</div>
                                    <div class="review-date">Hace 1 mes</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Rev 4 -->
                    <div class="review-card">
                        <div class="review-inner">
                            <span class="review-quote">"</span>
                            <div class="review-stars">★★★★★</div>
                            <p class="review-text">Pedimos la cena íntima para nuestro aniversario. El chef fue espectacular, muy amable y cada plato era una sorpresa de sabores chilenos gourmet.</p>
                            <div class="review-author">
                                <div class="review-avatar">VR</div>
                                <div>
                                    <div class="review-name">Valentina Rojas</div>
                                    <div class="review-date">Hace 2 meses</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Rev 5 -->
                    <div class="review-card">
                        <div class="review-inner">
                            <span class="review-quote">"</span>
                            <div class="review-stars">★★★★★</div>
                            <p class="review-text">Hamburguesas gigantes y muy buenas, las papas vienen con la porción perfecta. Excelente opción para los fines de semana.</p>
                            <div class="review-author">
                                <div class="review-avatar">LM</div>
                                <div>
                                    <div class="review-name">Luis Morales</div>
                                    <div class="review-date">Hace 2 meses</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="carousel-nav" id="reviews-dots"></div>
        </div>
    </section>

    <!-- ═══ IG GALLERY ═══ -->
    <section class="gallery-section reveal">
        <p class="section-label" style="justify-content: center; margin-bottom: 2rem;">Nuestra galería @lefranfood</p>
        <div class="gallery-grid" id="gallery-grid">
            <!-- 9 IG Placholders. /* ACA VAN LAS URLs DE IG REALES */ -->
            <div class="ig-item" onclick="openLightbox(0)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Torta Lefrán">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(1)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1626230606410-b97ac3cc856c?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Empanadas chilenas">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(2)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Hamburguesa artesanal">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(3)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Catering y banquetería">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(4)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1542826438-bd32f43d626f?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Pastel de frutas">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(5)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Torta de chocolate">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(6)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Postre mil hojas">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(7)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1555243896-c709bfa0b564?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Chef en evento">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
            <div class="ig-item" onclick="openLightbox(8)">
                <img loading="lazy" src="https://images.unsplash.com/photo-1559564114-065e94f83c13?q=80&w=1000&auto=format&fit=crop" onerror="this.style.display='none'" alt="Detalle de banquetería">
                <div class="ig-overlay"><span class="material-symbols-outlined">zoom_in_map</span></div>
            </div>
        </div>
    </section>

    <!-- Lightbox -->
    <div class="lightbox" id="lightbox">
        <button class="lb-close" onclick="closeLightbox()" aria-label="Cerrar">
            <span class="material-symbols-outlined">close</span>
        </button>
        <div class="lb-content">
            <button class="lb-prev" onclick="lbNavigate(-1)" aria-label="Anterior"><span class="material-symbols-outlined">chevron_left</span></button>
            <img src="" class="lb-img" id="lb-img" alt="">
            <button class="lb-next" onclick="lbNavigate(1)" aria-label="Siguiente"><span class="material-symbols-outlined">chevron_right</span></button>
        </div>
    </div>
"""

html = html.replace('<footer>', reviews_gallery_html + '\n    <footer>')

# Add scroll classes to banqueteria text/image
html = html.replace('<div class="banquet-visual">', '<div class="banquet-visual reveal-left">')
html = html.replace('<div class="banquet-copy">', '<div class="banquet-copy reveal-right">')
html = html.replace('<div class="pkg-card">', '<div class="pkg-card reveal">')
html = html.replace('<div class="pkg-card featured">', '<div class="pkg-card featured reveal">')

# 4. JS Additions
# - Update Data array with imgUrl and stock
old_products = """const products = [
            { id: 1, cat: 'tortas', name: 'Torta de frambuesa', desc: 'Suave bizcocho con crema fresca y frambuesas seleccionadas del sur.', price: 18000, img: '🍰' },
            { id: 2, cat: 'tortas', name: 'Torta de manjar', desc: 'Clásica torta chilena rellena de abundante manjar casero.', price: 16000, img: '🍮' },
            { id: 3, cat: 'tortas', name: 'Torta Red Velvet', desc: 'Aterciopelada y esponjosa, con auténtico frosting de queso crema.', price: 20000, img: '🎂' },
            { id: 4, cat: 'tortas', name: 'Torta de chocolate', desc: 'Para amantes del cacao, húmeda e intensa con ganache.', price: 17000, img: '🍫' },
            { id: 5, cat: 'tortas', name: 'Cheesecake frutos del bosque', desc: 'Pastel de queso horneado con coulis de frutos rojos.', price: 19000, img: '🫐' },
            { id: 6, cat: 'tortas', name: 'Torta personalizada', desc: 'Diseño a elección para cumpleaños, matrimonios y más.', price: 25000, img: '🎉', badge: 'Consultar' },
            { id: 7, cat: 'empanadas', name: 'Empanada de pino', desc: 'Receta tradicional con carne picada, aceitunas y huevo duro al horno.', price: 2700, img: '🥟' },
            { id: 8, cat: 'empanadas', name: 'Empanada de queso', desc: 'Masa horneada con abundante queso derretido por dentro.', price: 2500, img: '🧀' },
            { id: 9, cat: 'empanadas', name: 'Docena de empanadas', desc: 'Surtido a elección para compartir. ¡Consulta por variedades!', price: 12000, img: '📦' },
            { id: 10, cat: 'hamburguesas', name: 'Hamburguesa clásica', desc: 'Carne de res, queso, lechuga, tomate, papas fritas incluidas.', price: 7500, img: '🍔' },
            { id: 11, cat: 'hamburguesas', name: 'Hamburguesa de pollo', desc: 'Crujiente filete de pollo apanado, coleslaw y mayo chipotle.', price: 7500, img: '🍗' },
            { id: 12, cat: 'hamburguesas', name: 'Hamburguesa BBQ', desc: 'Doble tocino, aros de cebolla, queso cheddar y salsa BBQ.', price: 8500, img: '🥓' },
            { id: 13, cat: 'pasteles', name: 'Tarta de limón merengada', desc: 'Equilibrio entre acidez del limón y dulzura del merengue tostado.', price: 14000, img: '🍋' },
            { id: 14, cat: 'pasteles', name: 'Tarta de frutas', desc: 'Masa sablé, crema pastelera y fruta fresca de temporada.', price: 14000, img: '🍓' },
            { id: 15, cat: 'pasteles', name: 'Mil hojas', desc: 'Capas crujientes rellenas generosamente de manjar casero.', price: 13000, img: '🥧' },
        ];"""

new_products = """const products = [
            /* ACA VAN LAS URLS DE IG O IMAGENES PROPIAS DE LOS PRODUCTOS. 'stock' es null (ilimitado) o númerico */
            { id: 1, cat: 'tortas', name: 'Torta de frambuesa', desc: 'Suave bizcocho con crema fresca y frambuesas seleccionadas.', price: 18000, img: '🍰', imgUrl: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600', stock: null },
            { id: 2, cat: 'tortas', name: 'Torta de manjar', desc: 'Clásica torta chilena rellena de abundante manjar casero.', price: 16000, img: '🍮', imgUrl: '', stock: 12 },
            { id: 3, cat: 'tortas', name: 'Torta Red Velvet', desc: 'Aterciopelada y esponjosa, con auténtico frosting de queso crema.', price: 20000, img: '🎂', imgUrl: 'https://images.unsplash.com/photo-1616541823729-00fe0aacd32c?w=600', stock: 3 },
            { id: 4, cat: 'tortas', name: 'Torta de chocolate', desc: 'Para amantes del cacao, húmeda e intensa con ganache.', price: 17000, img: '🍫', imgUrl: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600', stock: null },
            { id: 5, cat: 'tortas', name: 'Cheesecake frutos del bosque', desc: 'Pastel de queso horneado con coulis de frutos rojos.', price: 19000, img: '🫐', imgUrl: 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=600', stock: 4 },
            { id: 6, cat: 'tortas', name: 'Torta personalizada', desc: 'Diseño a elección para cumpleaños, matrimonios y más.', price: 25000, img: '🎉', badge: 'Consultar', imgUrl: '', stock: null },
            { id: 7, cat: 'empanadas', name: 'Empanada de pino', desc: 'Receta tradicional con carne picada, aceitunas y huevo duro al horno.', price: 2700, img: '🥟', imgUrl: 'https://images.unsplash.com/photo-1626230606410-b97ac3cc856c?w=600', stock: 0 },
            { id: 8, cat: 'empanadas', name: 'Empanada de queso', desc: 'Masa horneada con abundante queso derretido por dentro.', price: 2500, img: '🧀', imgUrl: '', stock: null },
            { id: 9, cat: 'empanadas', name: 'Docena de empanadas', desc: 'Surtido a elección para compartir. ¡Consulta por variedades!', price: 12000, img: '📦', imgUrl: '', stock: null },
            { id: 10, cat: 'hamburguesas', name: 'Hamburguesa clásica', desc: 'Carne de res, queso, lechuga, tomate, papas fritas incluidas.', price: 7500, img: '🍔', imgUrl: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600', stock: null },
            { id: 11, cat: 'hamburguesas', name: 'Hamburguesa de pollo', desc: 'Crujiente filete de pollo apanado, coleslaw y mayo chipotle.', price: 7500, img: '🍗', imgUrl: '', stock: 5 },
            { id: 12, cat: 'hamburguesas', name: 'Hamburguesa BBQ', desc: 'Doble tocino, aros de cebolla, queso cheddar y salsa BBQ.', price: 8500, img: '🥓', imgUrl: 'https://images.unsplash.com/photo-1594212691516-7463f5ceaaec?w=600', stock: null },
            { id: 13, cat: 'pasteles', name: 'Tarta de limón merengada', desc: 'Equilibrio entre acidez del limón y dulzura del merengue tostado.', price: 14000, img: '🍋', imgUrl: 'https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600', stock: null },
            { id: 14, cat: 'pasteles', name: 'Tarta de frutas', desc: 'Masa sablé, crema pastelera y fruta fresca de temporada.', price: 14000, img: '🍓', imgUrl: 'https://images.unsplash.com/photo-1542826438-bd32f43d626f?w=600', stock: 2 },
            { id: 15, cat: 'pasteles', name: 'Mil hojas', desc: 'Capas crujientes rellenas generosamente de manjar casero.', price: 13000, img: '🥧', imgUrl: '', stock: null },
        ];"""

html = html.replace(old_products, new_products)

# Filter update
render_fn_old = """// ── RENDER PRODUCTS ──
        function renderProducts(filter) {
            currentFilter = filter;
            const grid = document.getElementById('product-grid');
            const banquet = document.getElementById('banquet-section');
            const label = document.getElementById('section-label');"""

render_fn_new = """// ── RENDER PRODUCTS ──
        function renderProducts(filter, searchText = '') {
            currentFilter = filter;
            const grid = document.getElementById('product-grid');
            const banquet = document.getElementById('banquet-section');
            const label = document.getElementById('section-label');"""
            
html = html.replace(render_fn_old, render_fn_new)

list_old = """const list = filter === 'todos' ? products : products.filter(p => p.cat === filter);

            const labels = { todos: 'Nuestros productos', tortas: 'Tortas artesanales', empanadas: 'Empanadas', hamburguesas: 'Hamburguesas', pasteles: 'Pasteles & tartas' };
            label.textContent = labels[filter] || 'Productos';

            grid.innerHTML = '';
            list.forEach((p, i) => {"""

list_new = """let list = filter === 'todos' ? products : products.filter(p => p.cat === filter);
            if(searchText.trim() !== '') {
                const term = searchText.toLowerCase().trim();
                list = list.filter(p => p.name.toLowerCase().includes(term) || p.desc.toLowerCase().includes(term));
            }

            const labels = { todos: 'Nuestros productos', tortas: 'Tortas artesanales', empanadas: 'Empanadas', hamburguesas: 'Hamburguesas', pasteles: 'Pasteles & tartas' };
            label.textContent = labels[filter] || 'Productos';

            grid.innerHTML = '';
            
            if(list.length === 0) {
                grid.innerHTML = `<div class="no-results">
                    <span class="material-symbols-outlined" style="font-size:3rem;opacity:0.5;">search_off</span>
                    <p style="margin-top:1rem;margin-bottom:1.5rem;">No encontramos productos para tu búsqueda.</p>
                    <button class="btn-outline" style="margin:0 auto;" onclick="document.getElementById('search-input').value=''; handleSearch();">Ver todos</button>
                </div>`;
                return;
            }

            list.forEach((p, i) => {
                const searchInCart = cart.find(x => x.id === p.id);
                const currentQty = searchInCart ? searchInCart.qty : 0;
                
                // Stock logic
                let stockBadge = '';
                let isOut = false;
                if(p.stock !== null && p.stock !== undefined) {
                    const available = p.stock - currentQty;
                    if(available <= 0) {
                        stockBadge = `<div class="card-stock stock-out">Agotado</div>`;
                        isOut = true;
                    } else if(available <= 5) {
                        stockBadge = `<div class="card-stock stock-low">Últimas ${available} unidades</div>`;
                    } else {
                        stockBadge = `<div class="card-stock stock-ok">Disponible</div>`;
                    }
                }

                // Image logic
                const imgReal = p.imgUrl && p.imgUrl.trim() !== '' ? 
                        `<img src="${p.imgUrl}" loading="lazy" onerror="this.style.display='none'">` : '';
"""
html = html.replace(list_old, list_new)


btn_old = """const btn = `<button class="add-btn" onclick="addToCart(${p.id})" id="addbtn-${p.id}">
      <span class="material-symbols-outlined" style="font-size:1rem;">add_shopping_cart</span> Agregar
    </button>`;
                const el = document.createElement('div');
                el.className = 'card';
                el.style.animationDelay = `${i * 0.06}s`;
                el.innerHTML = `
      <div class="card-img">${badge}${p.img}</div>
      <div class="card-body">"""

btn_new = """const btn = isOut ? 
                    `<button class="add-btn" style="background:var(--surface2);color:var(--muted);cursor:not-allowed;" disabled><span class="material-symbols-outlined" style="font-size:1rem;">block</span> Agotado</button>` :
                    `<button class="add-btn" onclick="addToCart(${p.id})" id="addbtn-${p.id}">
                      <span class="material-symbols-outlined" style="font-size:1rem;">add_shopping_cart</span> Agregar
                    </button>`;
                const el = document.createElement('div');
                el.className = 'card reveal'; // Added reveal class for entrance animations
                el.style.animationDelay = `${(i % 5) * 0.06}s`;
                el.innerHTML = `
      <div class="card-img">
        <div class="card-img-fallback">${p.img}</div>
        ${imgReal}
        <div class="card-img-overlay"></div>
        ${badge}
        ${stockBadge}
      </div>
      <div class="card-body">"""
html = html.replace(btn_old, btn_new)


# Persistence & rest logic
script_end_old = """// ── INIT ──
        document.addEventListener('DOMContentLoaded', () => {
            renderProducts('todos');
            updateCart();
            // hide banquet section initially
            document.getElementById('banquet-section').style.display = 'none';
        });
    </script>"""

script_end_new = """// ── PERSISTENCE (LocalStorage) ──
        function saveCart() {
            localStorage.setItem('lefran_cart', JSON.stringify(cart));
        }
        function loadCart() {
            const sc = localStorage.getItem('lefran_cart');
            if(sc) {
                try {
                    const parsed = JSON.parse(sc);
                    // validate vs products
                    cart = parsed.filter(c => products.some(p => p.id === c.id));
                    if(cart.length > 0) {
                        setTimeout(() => showToast(`Tienes ${cart.length} productos guardados en tu carrito.`), 1000);
                    }
                } catch(e) { cart = []; }
            }
        }

        // ── OVERRIDE CART UPDATES TO SAVE AND RE-RENDER STOCK ──
        const origUpdateCart = updateCart;
        updateCart = function() {
            origUpdateCart();
            saveCart();
            // Re-render to update stock limits dynamically across grid
            const srchEl = document.getElementById('search-input');
            const searchVal = srchEl ? srchEl.value : '';
            renderProducts(currentFilter, searchVal);
            setupAnimations();
        }

        // ── SEARCH ──
        function handleSearch() {
            const val = document.getElementById('search-input').value;
            // sync mobile
            const mob = document.getElementById('search-input-mobile');
            if(mob) mob.value = val;
            renderProducts(currentFilter, val);
            setupAnimations();
        }
        function handleSearchMobile() {
            const val = document.getElementById('search-input-mobile').value;
            // sync desktop
            const desk = document.getElementById('search-input');
            if(desk) desk.value = val;
            renderProducts(currentFilter, val);
            setupAnimations();
        }

        // ── THEME TOGGLE ──
        function toggleTheme() {
            const d = document.documentElement;
            const icon = document.getElementById('theme-icon');
            if (d.getAttribute('data-theme') === 'light') {
                d.removeAttribute('data-theme');
                localStorage.setItem('lefran_theme', 'dark');
                icon.textContent = 'light_mode';
            } else {
                d.setAttribute('data-theme', 'light');
                localStorage.setItem('lefran_theme', 'light');
                icon.textContent = 'dark_mode';
            }
        }

        function loadTheme() {
            const t = localStorage.getItem('lefran_theme');
            if(t === 'light') {
                document.documentElement.setAttribute('data-theme', 'light');
                const i = document.getElementById('theme-icon');
                if(i) i.textContent = 'dark_mode';
            }
        }

        // ── MARQUEE BANNER ──
        function closePromo() {
            const b = document.getElementById('promo-banner');
            b.classList.add('closed');
            sessionStorage.setItem('promo_closed', 'true');
        }

        // ── REVIEWS CAROUSEL ──
        let rIndex = 0;
        let rInterval;
        function setupReviews() {
            const t = document.getElementById('reviews-track');
            const d = document.getElementById('reviews-dots');
            const cards = document.querySelectorAll('.review-card');
            if(!cards.length || !d) return;
            
            // clear dots if recall
            d.innerHTML = '';
            
            // setup dots
            cards.forEach((_, i) => {
                const dot = document.createElement('div');
                dot.className = i===0 ? 'c-dot active' : 'c-dot';
                dot.onclick = () => { rIndex=i; updateRev(); resetRInterval(); };
                d.appendChild(dot);
            });
            
            function updateRev() {
                // Determine items per view
                let w = window.innerWidth;
                let vis = w >= 1024 ? 3 : (w >= 768 ? 2 : 1);
                let max = cards.length - vis;
                if(max < 0) max = 0;
                if(rIndex > max) rIndex = 0;
                
                t.style.transform = `translateX(-${(100/cards.length) * rIndex}%)`;
                document.querySelectorAll('.c-dot').forEach((dt,idx) => {
                    dt.className = idx===rIndex ? 'c-dot active':'c-dot';
                });
                cards.forEach((c,idx) => c.classList.toggle('active', idx>=rIndex && idx<rIndex+vis));
            }
            
            function autoRun() {
                let w = window.innerWidth;
                let vis = w >= 1024 ? 3 : (w >= 768 ? 2 : 1);
                let max = cards.length - vis;
                rIndex++;
                if(rIndex > max) rIndex = 0;
                updateRev();
            }
            
            rInterval = setInterval(autoRun, 4000);
            function resetRInterval() { clearInterval(rInterval); rInterval = setInterval(autoRun, 4000); }
            window.addEventListener('resize', updateRev);
            updateRev();
        }

        // ── LIGHTBOX GALLERY ──
        const galleryImgs = Array.from(document.querySelectorAll('.ig-item img')).map(img => img.src);
        let lbIndex = 0;
        function openLightbox(idx) {
            if(!galleryImgs[idx]) return;
            lbIndex = idx;
            document.getElementById('lb-img').src = galleryImgs[lbIndex];
            document.getElementById('lightbox').classList.add('active');
        }
        function closeLightbox() {
            document.getElementById('lightbox').classList.remove('active');
            setTimeout(()=> { document.getElementById('lb-img').src=''; }, 300);
        }
        function lbNavigate(dir) {
            lbIndex += dir;
            if(lbIndex < 0) lbIndex = galleryImgs.length - 1;
            if(lbIndex >= galleryImgs.length) lbIndex = 0;
             document.getElementById('lb-img').src = galleryImgs[lbIndex];
        }
        // global click lb
        document.getElementById('lightbox')?.addEventListener('click', e => {
            if(e.target.id === 'lightbox') closeLightbox();
        });
        document.addEventListener('keydown', e => {
            if(e.key === 'Escape' && document.getElementById('lightbox').classList.contains('active')) closeLightbox();
            if(e.key === 'ArrowLeft' && document.getElementById('lightbox').classList.contains('active')) lbNavigate(-1);
            if(e.key === 'ArrowRight' && document.getElementById('lightbox').classList.contains('active')) lbNavigate(1);
        });

        // ── SCROLL ANIMATIONS (Intersection Observer) ──
        function setupAnimations() {
            const obs = new IntersectionObserver((entries, observer) => {
                entries.forEach(e => {
                    if(e.isIntersecting) {
                        e.target.classList.add('active');
                        observer.unobserve(e.target);
                    }
                });
            }, { rootMargin: '0px 0px -50px 0px', threshold: 0.1 });
            
            document.querySelectorAll('.reveal:not(.active), .reveal-left:not(.active), .reveal-right:not(.active)').forEach(el => obs.observe(el));
        }

        // ── INIT ──
        document.addEventListener('DOMContentLoaded', () => {
            loadTheme();
            if(sessionStorage.getItem('promo_closed')) {
                const b = document.getElementById('promo-banner');
                if(b) b.classList.add('closed');
            }
            loadCart();
            renderProducts('todos', '');
            updateCart();
            document.getElementById('banquet-section').style.display = 'none';
            setupReviews();
            setTimeout(setupAnimations, 100);
        });
    </script>"""

html = html.replace(script_end_old, script_end_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Changes applied successfully.")
