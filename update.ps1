$globalHeader = '<header class="site-header" style="background-color: #0f4c3a; color: #ffffff; padding: 12px 20px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.15);"><div class="nav-container" style="max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;"><a href="index.html" style="font-size: 1.4rem; font-weight: 800; color: #ffffff; text-decoration: none;">?? MATCHA MAYA</a><nav class="main-nav"><ul style="display: flex; list-style: none; gap: 10px; padding: 0; margin: 0;"><li><a href="index.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">?? Home</a></li><li><a href="index2.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">??? 220 Interviews</a></li><li><a href="comparison.html" style="text-decoration: none; color: #ffffff; font-weight: 600; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.3); background: rgba(255,255,255,0.08); font-size: 0.85rem;">?? Comparison</a></li></ul></nav><div class="search-box"><input type="text" id="citySearch" placeholder="?? Search cities..." onkeyup="filterCities()" style="padding: 6px 12px; border-radius: 20px; border: none; outline: none; font-size: 0.85rem;"></div></div></header><nav class="breadcrumb-trail" style="background: #eef5ee; padding: 8px 20px; font-size: 0.85rem; border-bottom: 1px solid #d1ded0;"><div style="max-width: 1400px; margin: 0 auto;"><a href="index.html" style="color: #2d5a27; text-decoration: none; font-weight: 600;">Home</a> &gt; <a href="index2.html" style="color: #2d5a27; text-decoration: none; font-weight: 600;">Interviews</a> &gt; <span style="color: #666;">City Breakdown</span></div></nav>'

Get-ChildItem -Filter *.html | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if ($content -match '(?s)<header class="site-header">.*?</header>') {
        $content = $content -replace '(?s)<header class="site-header">.*?</header>', $globalHeader
    } else {
        $content = $content -replace '<body>', "<body>`n$globalHeader"
    }
    Set-Content -Path $_.FullName -Value $content
}

$indexPath = "index2.html"
$filterScript = '<script>function filterCities() { let input = document.getElementById("citySearch").value.toLowerCase(); let cards = document.getElementsByClassName("guide-card"); for (let i = 0; i < cards.length; i++) { let cityName = cards[i].innerText.toLowerCase(); cards[i].style.display = cityName.includes(input) ? "" : "none"; } }</script></body>'

if (Test-Path $indexPath) {
    $content = Get-Content $indexPath -Raw
    if ($content -notmatch 'function filterCities') {
        $content = $content -replace '</body>', $filterScript
        Set-Content -Path $indexPath -Value $content
        Write-Host "Filter script injected into index2.html successfully!" -ForegroundColor Green
    }
}
