#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库结构优化脚本
解决重构后的遗留问题，清理冗余文件，优化目录结构
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

class KnowledgeBaseOptimizer:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.optimization_log = []
        self.total_operations = 0
        self.error_count = 0
        
        # 需要清理的旧目录
        self.legacy_dirs = [
            "Markdown使用说明", "bilibili", "html", "mindmaster", 
            "path", "test", "工作", "脚本", "background"
        ]
        
        # 需要移动的资源文件类型
        self.resource_extensions = {
            '.png': '01-图片资源',
            '.jpg': '01-图片资源', 
            '.jpeg': '01-图片资源',
            '.gif': '01-图片资源',
            '.pdf': '02-文档模板',
            '.doc': '02-文档模板',
            '.docx': '02-文档模板',
            '.xls': '02-文档模板',
            '.xlsx': '02-文档模板',
            '.zip': '04-安装包',
            '.rar': '04-安装包',
            '.exe': '03-软件工具'
        }
    
    def log_operation(self, operation, details):
        """记录操作日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {operation}: {details}"
        self.optimization_log.append(log_entry)
        print(log_entry)
        self.total_operations += 1
    
    def log_error(self, operation, error):
        """记录错误日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] ERROR - {operation}: {error}"
        self.optimization_log.append(log_entry)
        print(f"❌ {log_entry}")
        self.error_count += 1
    
    def clean_legacy_directories(self):
        """清理历史遗留目录"""
        print("\n🧹 清理历史遗留目录...")
        
        for legacy_dir in self.legacy_dirs:
            legacy_path = self.base_path / legacy_dir
            if legacy_path.exists():
                try:
                    # 移动到临时文件夹而不是删除
                    temp_dir = self.base_path / "07-临时文件" / "03-过期文件" / f"legacy_{legacy_dir}"
                    temp_dir.mkdir(parents=True, exist_ok=True)
                    
                    # 移动整个目录
                    shutil.move(str(legacy_path), str(temp_dir / legacy_dir))
                    self.log_operation("移动遗留目录", f"{legacy_dir} -> {temp_dir / legacy_dir}")
                    
                except Exception as e:
                    self.log_error("清理遗留目录", f"{legacy_dir}: {str(e)}")
            else:
                self.log_operation("检查遗留目录", f"{legacy_dir} - 不存在")
    
    def clean_node_modules(self):
        """清理冗余的node_modules文件"""
        print("\n🗑️ 清理冗余node_modules...")
        
        node_modules_paths = list(self.base_path.rglob("node_modules"))
        cleaned_count = 0
        
        for node_path in node_modules_paths:
            try:
                # 移动到临时文件而不是删除
                temp_dir = self.base_path / "07-临时文件" / "03-过期文件" / f"node_modules_{cleaned_count}"
                temp_dir.mkdir(parents=True, exist_ok=True)
                
                shutil.move(str(node_path), str(temp_dir))
                self.log_operation("移动node_modules", f"{node_path} -> {temp_dir}")
                cleaned_count += 1
                
            except Exception as e:
                self.log_error("清理node_modules", f"{node_path}: {str(e)}")
        
        print(f"✅ 清理了 {cleaned_count} 个node_modules目录")
    
    def organize_resource_files(self):
        """整理分散的资源文件"""
        print("\n📁 整理资源文件...")
        
        resource_dir = self.base_path / "06-资源素材"
        organized_count = 0
        
        # 遍历所有主要目录（跳过资源目录本身和临时目录）
        for main_dir in self.base_path.iterdir():
            if (main_dir.is_dir() and 
                main_dir.name.startswith(("00-", "01-", "02-", "03-", "04-", "05-")) and
                main_dir.name != "06-资源素材"):
                
                for file_path in main_dir.rglob("*"):
                    if file_path.is_file():
                        file_ext = file_path.suffix.lower()
                        
                        # 检查是否是需要移动的资源文件
                        if file_ext in self.resource_extensions:
                            try:
                                # 确定目标子目录
                                target_subdir = self.resource_extensions[file_ext]
                                target_dir = resource_dir / target_subdir
                                target_dir.mkdir(parents=True, exist_ok=True)
                                
                                # 保持相对路径结构
                                relative_path = file_path.relative_to(main_dir)
                                target_path = target_dir / f"{main_dir.name}_{relative_path}"
                                
                                # 确保目标目录存在
                                target_path.parent.mkdir(parents=True, exist_ok=True)
                                
                                # 移动文件
                                shutil.move(str(file_path), str(target_path))
                                self.log_operation("移动资源文件", f"{file_path} -> {target_path}")
                                organized_count += 1
                                
                            except Exception as e:
                                self.log_error("移动资源文件", f"{file_path}: {str(e)}")
        
        print(f"✅ 整理了 {organized_count} 个资源文件")
    
    def optimize_deep_directories(self):
        """优化过深的目录结构"""
        print("\n📊 优化深层目录结构...")
        
        # 找出深度超过7层的目录
        deep_dirs = []
        
        for root, dirs, files in os.walk(self.base_path):
            current_depth = root.count(os.sep) - str(self.base_path).count(os.sep)
            if current_depth > 7:
                deep_dirs.append((root, current_depth))
        
        # 按深度排序
        deep_dirs.sort(key=lambda x: x[1], reverse=True)
        
        optimized_count = 0
        for deep_dir, depth in deep_dirs[:10]:  # 只处理前10个最深的目录
            try:
                dir_path = Path(deep_dir)
                if dir_path.exists():
                    # 移动到临时文件
                    temp_dir = self.base_path / "07-临时文件" / "03-过期文件" / f"deep_dir_{optimized_count}"
                    temp_dir.mkdir(parents=True, exist_ok=True)
                    
                    shutil.move(str(dir_path), str(temp_dir))
                    self.log_operation("移动深层目录", f"深度{depth}: {dir_path} -> {temp_dir}")
                    optimized_count += 1
                    
            except Exception as e:
                self.log_error("优化深层目录", f"{deep_dir}: {str(e)}")
        
        print(f"✅ 优化了 {optimized_count} 个深层目录")
    
    def create_directory_readme(self):
        """为每个主要目录创建README说明文件"""
        print("\n📝 创建目录说明文件...")
        
        readme_templates = {
            "00-项目管理": """# 项目管理

本目录包含所有工作相关的项目管理文件。

## 子目录说明
- `01-工作报告`: 工作报告和总结文档
- `02-项目汇总`: 各个项目的技术文档和资料
- `03-报文文档`: 系统报文和接口文档
- `04-SQL脚本`: 数据库脚本和查询
- `05-邮件沟通`: 重要邮件沟通记录
- `06-工作资料`: 其他工作相关文档

## 使用规范
1. 新项目文档请按项目分类存放
2. 重要文档请定期备份
3. 过期项目请移至临时目录
""",
            
            "01-学习笔记": """# 学习笔记

本目录包含所有学习相关的资料和笔记。

## 子目录说明
- `01-读书笔记`: 各类书籍的阅读笔记
- `02-在线课程`: 网络课程学习资料
- `03-学习资料`: 技术文档和参考资料
- `04-练习项目`: 编程练习和实验项目

## 使用规范
1. 按学科或技术领域分类存放
2. 重要笔记建议使用Markdown格式
3. 代码练习请放在对应的项目目录中
""",
            
            "02-技术文档": """# 技术文档

本目录包含技术开发相关的文档资料。

## 子目录说明
- `01-开发文档`: 开发指南和最佳实践
- `02-系统配置`: 系统配置和环境设置
- `03-API文档`: 接口文档和数据格式
- `04-技术规范`: 编码规范和技术标准

## 使用规范
1. 文档请保持更新，确保信息准确
2. 重要变更请记录版本历史
3. 建议使用统一的文档模板
""",
            
            "03-脚本工具": """# 脚本工具

本目录包含各种实用的脚本和工具。

## 子目录说明
- `01-PowerShell脚本`: Windows PowerShell脚本
- `02-Python脚本`: Python自动化脚本
- `03-批处理脚本`: Windows批处理文件
- `04-其他工具`: 其他实用工具和脚本

## 使用规范
1. 脚本请添加必要的注释说明
2. 重要脚本请备份原始版本
3. 测试后再在生产环境使用
""",
            
            "04-问题记录": """# 问题记录

本目录包含问题排查和解决方案记录。

## 子目录说明
- `01-常见问题`: FAQ和常见问题解答
- `02-故障排查`: 系统故障排查记录
- `03-解决方案`: 问题的解决方案
- `04-经验总结`: 技术经验和最佳实践

## 使用规范
1. 问题记录请包含时间、现象、原因、解决方案
2. 相同问题请关联已有记录
3. 定期整理和更新解决方案
""",
            
            "05-文章创作": """# 文章创作

本目录包含原创文章和写作资料。

## 子目录说明
- `01-技术文章`: 技术分享和教程
- `02-游戏评测`: 游戏相关评测和体验
- `03-生活随笔`: 生活感悟和随笔
- `04-草稿箱`: 未完成的草稿和素材

## 使用规范
1. 原创文章请标注创作时间
2. 引用内容请注明来源
3. 定期整理草稿箱内容
""",
            
            "06-资源素材": """# 资源素材

本目录包含各种资源文件和素材。

## 子目录说明
- `01-图片资源`: 图片、截图等视觉素材
- `02-文档模板`: 各类文档模板和样例
- `03-软件工具`: 软件安装包和工具
- `04-安装包`: 各类软件安装程序

## 使用规范
1. 按类型和用途分类存放
2. 大文件请考虑压缩存储
3. 定期清理过期和无用文件
""",
            
            "07-临时文件": """# 临时文件

本目录包含临时和待整理的文件。

## 子目录说明
- `01-待整理`: 等待分类整理的文件
- `02-测试文件`: 各种测试和实验文件
- `03-过期文件`: 已过期但暂不删除的文件

## 使用规范
1. 定期清理和整理临时文件
2. 重要文件请及时分类到对应目录
3. 过期文件定期评估是否删除
"""
        }
        
        created_count = 0
        for dir_name, template in readme_templates.items():
            dir_path = self.base_path / dir_name
            if dir_path.exists():
                readme_path = dir_path / "README.md"
                if not readme_path.exists():
                    try:
                        with open(readme_path, 'w', encoding='utf-8') as f:
                            f.write(template)
                        self.log_operation("创建README", f"{readme_path}")
                        created_count += 1
                    except Exception as e:
                        self.log_error("创建README", f"{readme_path}: {str(e)}")
        
        print(f"✅ 创建了 {created_count} 个README文件")
    
    def generate_optimization_report(self):
        """生成优化报告"""
        report = {
            "optimization_time": datetime.now().isoformat(),
            "base_path": str(self.base_path),
            "total_operations": self.total_operations,
            "error_count": self.error_count,
            "optimization_log": self.optimization_log,
            "summary": {
                "legacy_dirs_cleaned": len(self.legacy_dirs),
                "node_modules_cleaned": self.optimization_log.count("移动node_modules"),
                "resource_files_organized": self.optimization_log.count("移动资源文件"),
                "deep_directories_optimized": self.optimization_log.count("移动深层目录"),
                "readme_files_created": self.optimization_log.count("创建README")
            }
        }
        
        report_path = self.base_path / "结构优化报告.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report
    
    def run_optimization(self):
        """运行完整的优化流程"""
        print("🚀 开始知识库结构优化...")
        print("=" * 50)
        
        try:
            # 1. 清理历史遗留目录
            self.clean_legacy_directories()
            
            # 2. 清理冗余node_modules
            self.clean_node_modules()
            
            # 3. 整理资源文件
            self.organize_resource_files()
            
            # 4. 优化深层目录结构
            self.optimize_deep_directories()
            
            # 5. 创建目录说明文件
            self.create_directory_readme()
            
            # 6. 生成优化报告
            report = self.generate_optimization_report()
            
            print("\n" + "=" * 50)
            print("✅ 结构优化完成!")
            print(f"📊 总操作数: {self.total_operations}")
            print(f"❌ 错误数: {self.error_count}")
            print(f"📄 详细报告已保存到: 结构优化报告.json")
            
            return report
            
        except Exception as e:
            print(f"❌ 优化过程中发生错误: {str(e)}")
            return None

def main():
    """主函数"""
    optimizer = KnowledgeBaseOptimizer()
    report = optimizer.run_optimization()
    
    if report:
        print("\n📋 优化摘要:")
        for key, value in report["summary"].items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()