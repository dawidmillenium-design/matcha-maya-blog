import os

tag = '<meta name="google-site-verification" content="ddryQTwrxDAxNvgfjcrTs2eW06UebOvdNums43rTfJc" />'

def process_directory(path="."):
    updated_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                if "ddryQTwrxDAxNvgfjcrTs2eW06UebOvdNums43rTfJc" not in content:
                    if "<head>" in content:
                        new_content = content.replace("<head>", f"<head>\n  {tag}")
                    elif "<HEAD>" in content:
                        new_content = content.replace("<HEAD>", f"<HEAD>\n  {tag}")
                    else:
                        continue

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    updated_count += 1

    print(f"SUCCESS: Added Google verification meta tag to {updated_count} HTML files!")

process_directory(".")
