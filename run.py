'''
将PDF文件批量转换为Markdown格式的脚本。
该脚本会遍历指定文件夹及其子文件夹中的所有PDF文件，
使用MarkItDown库将它们转换为Markdown格式，
并保存到output文件夹中。
注意：该脚本需要安装MarkItDown库，
可以使用以下命令安装：
pip install markitdown
'''
# 从source文件夹及其所有子文件夹中提取所有pdf文件，使用markitdown命令将其转换为markdown文件，保存到output文件夹中
import os
from markitdown import MarkItDown
# 定义源文件夹和目标文件夹

# 默认为'/Users/qinlang/Downloads/导出的条目'文件夹，如果文件夹为空将定义改为输入路径
if not os.listdir('/Users/qinlang/Downloads/导出的条目'):
    SOURCE_FOLDER = input('请输入源文件夹路径：')
else:
    SOURCE_FOLDER = 'source'
OUTPUT_FOLDER = 'output'
# 确保输出文件夹存在
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
#清空output文件夹
for root, dirs, files in os.walk(OUTPUT_FOLDER):
    for file in files:
        os.remove(os.path.join(root, file))
# 遍历源文件夹及其所有子文件夹中的所有文件
for root, dirs, files in os.walk(SOURCE_FOLDER):
    for filename in files:
        if filename.endswith('.pdf'):
            # 构建源文件和目标文件的完整路径
            source_file = os.path.join(root, filename)
            target_file = os.path.join(OUTPUT_FOLDER, filename.replace('.pdf', '.md')) # 替换文件扩展名
            # 初始化MarkItDown对象，设置为启用插件
            md = MarkItDown(enable_plugins=True)
            # 转换PDF文件为Markdown
            result = md.convert(source_file)
            # 将转换后的Markdown内容写入目标文件
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
