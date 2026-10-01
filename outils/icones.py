from playwright.sync_api import sync_playwright
import pathlib
R=pathlib.Path(__file__).resolve().parent.parent; p=(R/'index.html').as_uri()
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':512,'height':512})
    pg.goto(p); pg.wait_for_timeout(300)
    for name,size,pad in [('icon-512',512,0),('icon-maskable-512',512,1),('icon-192',192,0),('apple-touch-icon',180,0)]:
        pg.set_viewport_size({'width':size,'height':size})
        s = 1.6 if pad else 2.1
        pg.evaluate(f"""()=>{{document.body.style.cssText='margin:0;padding:0;background:#FFC93C';
          document.documentElement.style.padding='0';
          document.body.innerHTML=`<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512' width='{size}' height='{size}' style='display:block'>
          <rect width='512' height='512' fill='#FFC93C'/><circle cx='256' cy='256' r='{200 if pad else 236}' fill='#BFE3F2'/>
          <path d='M0 400 q256 -70 512 0 V512 H0z' fill='#7CC46A' opacity='{0 if pad else 1}'/>
          ${{DEFS}}${{dragon(236,330,{s},{{}})}}</svg>`;}}""")
        pg.wait_for_timeout(100)
        pg.screenshot(path=f'{R}/icons/{name}.png',clip={'x':0,'y':0,'width':size,'height':size})
    b.close()
