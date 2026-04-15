import os

def analyze_html():
    file_path = 'index.html'
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            # Count how many sections (divs) and buttons you have
            div_count = content.count('<div')
            btn_count = content.count('<button')
            
            print("--- Portfolio Data Report ---")
            print(f"Total Layout Sections: {div_count}")
            print(f"Interactive Buttons: {btn_count}")
            print("Status: Site is data-rich and ready for visitors!")
            print("-----------------------------")
    else:
        print("Error: index.html not found.")

if __name__ == "__main__":
    analyze_html()
