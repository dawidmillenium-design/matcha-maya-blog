# 1. Define clean single header without search box
$cleanHeader = @'
<header class="site-header" style="background-color: #0f4c3a; color: #ffffff; padding: 12px 20px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.15);">
  <div class="nav-container" style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <a href="index.html" style="font-size: 1.4rem; font-weight: 800; color: #ffffff; text-decoration: none;">MATCHA MAYA</a>
    <nav class="main-nav">
      <ul style="display: flex; list-style: none; gap: 10px; padding: 0; margin: 0;">
        <li><a href="index.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">Home</a></li>
        <li><a href="index2.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">220 Interviews</a></li>
        <li><a href="comparison.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">Comparison</a></li>
      </ul>
    </nav>
  </div>
</header>
