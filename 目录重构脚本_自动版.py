#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
个人知识库目录结构重构脚本 - 自动执行版本
将当前混乱的目录结构重组为规范的知识库结构
"""

import os
import shutil
import json
from pathlib import Path
from typing import Dict, List, Tuple

class KnowledgeBaseRestructurer:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.migration_log = []
        self.error_log = []
        
        # 新目录结构定义
        self.new_structure = {
            "00-项目管理": {
                "01-工作报告": {},
                "02-项目汇总": {
                    "01-跨环境项目": {},
                    "02-A1区项目": {},
                    "03-A2区项目": {},
                    "04-A3区项目": {},
                    "05-A4区项目": {},
                    "06-其他项目": {}
                },
                "03-报文文档": {},
                "04-SQL脚本": {
                    "01-服务器迁移": {},
                    "02-跨环境临时使用": {},
                    "03-常用脚本": {}
                },
                "05-邮件沟通": {},
                "06-工作资料": {
                    "01-HTML文档": {},
                    "02-PDF文档": {}
                }
            },
            "01-学习笔记": {
                "01-读书笔记": {
                    "01-技术书籍": {},
                    "02-管理书籍": {},
                    "03-其他书籍": {}
                },
                "02-在线课程": {},
                "03-学习资料": {
                    "01-Python学习": {},
                    "02-软件开发": {},
                    "03-其他技术": {}
                },
                "04-练习项目": {
                    "01-todo应用": {}
                }
            },
            "02-技术文档": {
                "01-开发文档": {},
                "02-系统配置": {},
                "03-API文档": {},
                "04-技术规范": {}
            },
            "03-脚本工具": {
                "01-PowerShell脚本": {
                    "01-系统管理": {},
                    "02-网络工具": {},
                    "03-数据处理": {},
                    "04-格式转换": {}
                },
                "02-Python脚本": {},
                "03-批处理脚本": {},
                "04-其他工具": {}
            },
            "04-问题记录": {
                "01-常见问题": {
                    "01-AGV相关": {},
                    "02-系统问题": {},
                    "03-软件使用": {}
                },
                "02-故障排查": {},
                "03-解决方案": {},
                "04-经验总结": {}
            },
            "05-文章创作": {
                "01-技术文章": {},
                "02-游戏评测": {},
                "03-生活随笔": {},
                "04-草稿箱": {}
            },
            "06-资源素材": {
                "01-图片资源": {
                    "01-工作相关": {},
                    "02-学习资料": {},
                    "03-其他图片": {}
                },
                "02-文档模板": {},
                "03-软件工具": {},
                "04-安装包": {}
            },
            "07-临时文件": {
                "01-待整理": {},
                "02-测试文件": {},
                "03-过期文件": {}
            }
        }
        
        # 文件迁移映射规则
        self.migration_rules = {
            # 工作相关
            "工作/报告": "00-项目管理/01-工作报告",
            "工作/项目汇总/跨环境项目": "00-项目管理/02-项目汇总/01-跨环境项目",
            "工作/项目汇总/A1": "00-项目管理/02-项目汇总/02-A1区项目",
            "工作/项目汇总/A2": "00-项目管理/02-项目汇总/03-A2区项目",
            "工作/项目汇总/A3": "00-项目管理/02-项目汇总/04-A3区项目",
            "工作/项目汇总/A4": "00-项目管理/02-项目汇总/05-A4区项目",
            "工作/项目汇总/其他项目": "00-项目管理/02-项目汇总/06-其他项目",
            "工作/报文": "00-项目管理/03-报文文档",
            "工作/SQL/服务器迁移": "00-项目管理/04-SQL脚本/01-服务器迁移",
            "工作/SQL/跨环境临时使用": "00-项目管理/04-SQL脚本/02-跨环境临时使用",
            "工作/SQL": "00-项目管理/04-SQL脚本/03-常用脚本",
            "工作/邮件": "00-项目管理/05-邮件沟通",
            "工作/html": "00-项目管理/06-工作资料/01-HTML文档",
            "工作/pdf": "00-项目管理/06-工作资料/02-PDF文档",
            
            # 学习相关
            "读书笔记": "01-学习笔记/01-读书笔记",
            "阅读": "01-学习笔记/03-学习资料",
            "python": "01-学习笔记/03-学习资料/01-Python学习",
            "study": "01-学习笔记/04-练习项目",
            
            # 脚本工具
            "脚本/powershell脚本": "03-脚本工具/01-PowerShell脚本",
            "脚本/python": "03-脚本工具/02-Python脚本",
            
            # 问题记录
            "问题记录": "04-问题记录",
            
            # 文章创作
            "文章": "05-文章创作",
            
            # 资源素材
            "安装包": "06-资源素材/04-安装包"
        }
    
    def create_directory_structure(self):
        """创建新的目录结构"""
        print("正在创建新的目录结构...")
        
        def create_dirs(structure: Dict, base_path: Path):
            for dir_name, sub_dirs in structure.items():
                dir_path = base_path / dir_name
                try:
                    dir_path.mkdir(parents=True, exist_ok=True)
                    self.migration_log.append(f"创建目录: {dir_path}")
                    if sub_dirs:
                        create_dirs(sub_dirs, dir_path)
                except Exception as e:
                    self.error_log.append(f"创建目录失败 {dir_path}: {str(e)}")
        
        create_dirs(self.new_structure, self.base_path)
        print("目录结构创建完成")
    
    def migrate_files(self):
        """迁移文件到新目录"""
        print("开始迁移文件...")
        
        for source_pattern, target_dir in self.migration_rules.items():
            source_path = self.base_path / source_pattern
            
            if not source_path.exists():
                self.migration_log.append(f"源路径不存在: {source_path}")
                continue
            
            target_path = self.base_path / target_dir
            
            try:
                if source_path.is_file():
                    # 迁移单个文件
                    self._migrate_file(source_path, target_path)
                elif source_path.is_dir():
                    # 迁移整个目录
                    self._migrate_directory(source_path, target_path)
            except Exception as e:
                self.error_log.append(f"迁移失败 {source_path} -> {target_path}: {str(e)}")
        
        print("文件迁移完成")
    
    def _migrate_file(self, source_file: Path, target_dir: Path):
        """迁移单个文件"""
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / source_file.name
        
        # 处理文件名冲突
        counter = 1
        while target_file.exists():
            stem = source_file.stem
            suffix = source_file.suffix
            target_file = target_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        shutil.move(str(source_file), str(target_file))
        self.migration_log.append(f"迁移文件: {source_file} -> {target_file}")
    
    def _migrate_directory(self, source_dir: Path, target_dir: Path):
        """迁移整个目录"""
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for item in source_dir.iterdir():
            if item.is_file():
                self._migrate_file(item, target_dir)
            elif item.is_dir():
                # 递归迁移子目录
                sub_target = target_dir / item.name
                self._migrate_directory(item, sub_target)
        
        # 如果源目录为空，删除它
        try:
            if not any(source_dir.iterdir()):
                source_dir.rmdir()
                self.migration_log.append(f"删除空目录: {source_dir}")
        except OSError:
            pass  # 目录不为空或其他错误，忽略
    
    def handle_special_files(self):
        """处理特殊文件和资源"""
        print("处理特殊文件和资源...")
        
        # 处理根目录的特殊文件
        special_files = [
            "了不起的Markdown.md",
            ".vscode"
        ]
        
        for file_name in special_files:
            source_path = self.base_path / file_name
            if source_path.exists():
                if file_name.startswith('.'):
                    # 隐藏文件保持在根目录
                    self.migration_log.append(f"保留特殊文件: {file_name}")
                else:
                    # 其他文件移动到临时目录
                    target_path = self.base_path / "07-临时文件/01-待整理" / file_name
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(source_path), str(target_path))
                    self.migration_log.append(f"移动特殊文件: {file_name} -> 临时文件")
    
    def cleanup_empty_directories(self):
        """清理空目录"""
        print("清理空目录...")
        
        def remove_empty_dirs(path: Path):
            try:
                for item in path.iterdir():
                    if item.is_dir():
                        remove_empty_dirs(item)
                        if not any(item.iterdir()):
                            item.rmdir()
                            self.migration_log.append(f"删除空目录: {item}")
            except OSError:
                pass  # 忽略无法删除的目录
        
        # 清理原始目录结构中的空目录
        old_dirs = ["工作", "读书笔记", "阅读", "python", "study", "脚本", "问题记录", "文章", "安装包"]
        for dir_name in old_dirs:
            dir_path = self.base_path / dir_name
            if dir_path.exists() and dir_path.is_dir():
                remove_empty_dirs(dir_path)
    
    def generate_migration_report(self):
        """生成迁移报告"""
        report = {
            "migration_time": str(Path.cwd()),
            "total_operations": len(self.migration_log),
            "error_count": len(self.error_log),
            "migration_log": self.migration_log,
            "error_log": self.error_log
        }
        
        report_file = self.base_path / "迁移报告.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"迁移报告已保存到: {report_file}")
        return report
    
    def run_restructure(self):
        """执行完整的重构流程"""
        print("开始执行知识库目录结构重构...")
        print("=" * 50)
        
        try:
            # 1. 创建新目录结构
            self.create_directory_structure()
            print()
            
            # 2. 迁移文件
            self.migrate_files()
            print()
            
            # 3. 处理特殊文件
            self.handle_special_files()
            print()
            
            # 4. 清理空目录
            self.cleanup_empty_directories()
            print()
            
            # 5. 生成报告
            report = self.generate_migration_report()
            
            print("=" * 50)
            print("重构完成!")
            print(f"总操作数: {report['total_operations']}")
            print(f"错误数: {report['error_count']}")
            
            if report['error_count'] > 0:
                print("警告: 存在错误，请查看迁移报告详情")
            
        except Exception as e:
            print(f"重构过程中发生错误: {str(e)}")
            self.error_log.append(f"重构过程错误: {str(e)}")
            self.generate_migration_report()

def main():
    """主函数 - 自动执行版本"""
    print("个人知识库目录结构重构工具 - 自动执行版本")
    print("=" * 50)
    print("开始自动重构...")
    
    # 执行重构
    restructurer = KnowledgeBaseRestructurer()
    restructurer.run_restructure()

if __name__ == "__main__":
    main()