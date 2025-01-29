import markdown2
import json

def parse_markdown_to_json(markdown_content):
    """
    使用 markdown2 库将 Markdown 内容转换为 JSON 格式。
    
    参数:
    markdown_content (str): 包含 Markdown 内容的字符串
    
    返回:
    dict: 包含转换后 JSON 数据的字典
    """
    
    # 将 Markdown 转换为 HTML
    html = markdown2.markdown(markdown_content)
    
    # 初始化结果列表
    result = []
    
    # 简单解析 HTML 并构建 JSON 结构
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag in soup.find_all(['h1', 'h2', 'p', 'img']):
        item = {
            "type": tag.name,
            "content": tag.get_text(strip=True) if tag.name != 'img' else tag['src']
        }
        
        # 为每个元素类型添加额外的属性
        if tag.name == 'p':
            item["style"] = {"color": "black", "fontSize": "16px"}  # 默认值
        elif tag.name == 'img':
            item["alt"] = tag.get('alt', '')  # 添加 alt 属性，如果没有则为空字符串
        
        result.append(item)
    
    return {"content": result}

def main():
    """
    主函数：读取 Markdown 文件，调用解析函数，并将结果保存为 JSON 文件。
    """
    
    input_file_path = r"C:\Users\zty20\Desktop\md测试1.md"  # 输入 Markdown 文件路径
    output_file_path = r"C:\Users\zty20\Desktop\output.json"  # 输出 JSON 文件路径
    
    try:
        # 读取 Markdown 文件内容
        with open(input_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # 解析 Markdown 并生成 JSON 数据
        json_data = parse_markdown_to_json(markdown_content)
        
        # 将 JSON 数据写入文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        
        print(f"Conversion completed successfully. Output saved to {output_file_path}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()