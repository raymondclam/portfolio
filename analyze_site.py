import os

def analyze_html():
    # This now looks for ANY .html file in your folder
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print("--- Portfolio Data Report ---")
    for file_path in html_files:
        with open(file_path, 'r') as f:
            content = f.read()
            div_count = content.count('<div')
            btn_count = content.count('<button')
            print(f"File: {file_path} | Sections: {div_count} | Buttons: {btn_count}")
    
    print("Status: Multi-page analysis complete!")
    print("-----------------------------")

if __name__ == "__main__":
    analyze_html()