#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库目录结构验证脚本
验证重构后的目录结构是否符合预期，并提供管理建议
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

class KnowledgeBaseValidator:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.validation_results = []
        self.warnings = []
        self.suggestions = []
        
        # 理想的目录结构
        self.expected_structure = {
            "00-项目管理": ["01-工作报告", "02-项目汇总", "03-报文文档", "04-SQL脚本", "05-邮件沟通", "06-工作资料"],
            "01-学习笔记": ["01-读书笔记", "02-在线课程", "03-学习资料", "04-练习项目"],
            "02-技术文档": ["01-开发文档", "02-系统配置", "03-API文档", "04-技术规范"],
            "03-脚本工具": ["01-PowerShell脚本", "02-Python脚本", "03-批处理脚本", "04-其他工具"],
            "04-问题记录": ["01-常见问题", "02-故障排查", "03-解决方案", "04-经验总结"],
            "05-文章创作": ["01-技术文章", "02-游戏评测", "03-生活随笔", "04-草稿箱"],
            "06-资源素材": ["01-图片资源", "02-文档模板", "03-软件工具", "04-安装包"],
            "07-临时文件": ["01-待整理", "02-测试文件", "03-过期文件"]
        }
    
    def validate_directory_structure(self):
        """验证目录结构"""
        print("验证目录结构...")
        
        # 检查顶级目录
        top_level_dirs = [d for d in self.base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
        top_level_names = [d.name for d in top_level_dirs]
        
        # 检查是否包含所有预期目录
        for expected_dir in self.expected_structure.keys():
            if expected_dir in top_level_names:
                self.validation_results.append(f"✓ 找到预期目录: {expected_dir}")
                
                # 检查子目录
                expected_subdirs = self.expected_structure[expected_dir]
                actual_subdirs = [d.name for d in (self.base_path / expected_dir).iterdir() if d.is_dir()]
                
                for subdir in expected_subdirs:
                    if subdir in actual_subdirs:
                        self.validation_results.append(f"  ✓ 找到预期子目录: {expected_dir}/{subdir}")
                    else:
                        self.warnings.append(f"  ⚠ 缺少子目录: {expected_dir}/{subdir}")
                
                # 检查是否有额外的子目录
                extra_subdirs = set(actual_subdirs) - set(expected_subdirs)
                for subdir in extra_subdirs:
                    self.suggestions.append(f"  ? 额外子目录: {expected_dir}/{subdir}")
            else:
                self.warnings.append(f"✗ 缺少预期目录: {expected_dir}")
        
        # 检查是否有额外的顶级目录
        extra_dirs = set(top_level_names) - set(self.expected_structure.keys())
        for dir_name in extra_dirs:
            if not dir_name.startswith('.') and dir_name not in ['__pycache__']:
                self.suggestions.append(f"? 额外目录: {dir_name}")
    
    def analyze_file_distribution(self):
        """分析文件分布情况"""
        print("分析文件分布...")
        
        file_stats = defaultdict(lambda: {'count': 0, 'size': 0, 'types': defaultdict(int)})
        total_files = 0
        total_size = 0
        
        for root, dirs, files in os.walk(self.base_path):
            # 跳过隐藏目录和系统目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                file_path = Path(root) / file
                file_size = file_path.stat().st_size
                file_ext = file_path.suffix.lower()
                
                # 计算相对路径
                rel_path = file_path.relative_to(self.base_path)
                top_dir = rel_path.parts[0] if len(rel_path.parts) > 0 else "root"
                
                file_stats[top_dir]['count'] += 1
                file_stats[top_dir]['size'] += file_size
                file_stats[top_dir]['types'][file_ext] += 1
                
                total_files += 1
                total_size += file_size
        
        # 生成分布报告
        self.validation_results.append(f"\n文件分布统计:")
        self.validation_results.append(f"总文件数: {total_files}")
        self.validation_results.append(f"总大小: {self._format_size(total_size)}")
        
        for dir_name, stats in sorted(file_stats.items()):
            if dir_name in self.expected_structure or dir_name == "root":
                percentage = (stats['count'] / total_files) * 100
                self.validation_results.append(f"\n{dir_name}:")
                self.validation_results.append(f"  文件数: {stats['count']} ({percentage:.1f}%)")
                self.validation_results.append(f"  大小: {self._format_size(stats['size'])}")
                
                # 显示主要文件类型
                if stats['types']:
                    main_types = sorted(stats['types'].items(), key=lambda x: x[1], reverse=True)[:5]
                    types_str = ", ".join([f"{ext}({count})" for ext, count in main_types])
                    self.validation_results.append(f"  主要类型: {types_str}")
    
    def check_naming_consistency(self):
        """检查命名一致性"""
        print("检查命名一致性...")
        
        naming_issues = []
        
        for root, dirs, files in os.walk(self.base_path):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            # 检查目录命名
            for dir_name in dirs:
                if not self._is_valid_naming(dir_name):
                    naming_issues.append(f"目录命名不规范: {Path(root) / dir_name}")
            
            # 检查文件命名
            for file in files:
                if not file.startswith('.') and not self._is_valid_filename(file):
                    naming_issues.append(f"文件命名不规范: {Path(root) / file}")
        
        if naming_issues:
            self.warnings.append("\n命名规范性问题:")
            for issue in naming_issues[:10]:  # 只显示前10个
                self.warnings.append(f"  ⚠ {issue}")
            if len(naming_issues) > 10:
                self.warnings.append(f"  ... 还有 {len(naming_issues) - 10} 个命名问题")
        else:
            self.validation_results.append("✓ 命名规范性检查通过")
    
    def check_depth_complexity(self):
        """检查目录深度复杂度"""
        print("检查目录深度复杂度...")
        
        depth_stats = defaultdict(int)
        max_depth = 0
        deep_paths = []
        
        for root, dirs, files in os.walk(self.base_path):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            current_depth = root.count(os.sep) - str(self.base_path).count(os.sep)
            depth_stats[current_depth] += 1
            
            if current_depth > max_depth:
                max_depth = current_depth
            
            if current_depth > 4:  # 超过4层认为过深
                deep_paths.append(root)
        
        self.validation_results.append(f"\n目录深度分析:")
        self.validation_results.append(f"最大深度: {max_depth} 层")
        
        for depth, count in sorted(depth_stats.items()):
            self.validation_results.append(f"第 {depth} 层: {count} 个目录")
        
        if deep_paths:
            self.suggestions.append("\n过深的目录路径:")
            for path in deep_paths[:5]:  # 只显示前5个
                self.suggestions.append(f"  ? {path}")
            if len(deep_paths) > 5:
                self.suggestions.append(f"  ... 还有 {len(deep_paths) - 5} 个深层目录")
    
    def generate_management_suggestions(self):
        """生成管理建议"""
        print("生成管理建议...")
        
        suggestions = []
        
        # 基于文件分布的建议
        suggestions.append("\n📋 管理建议:")
        suggestions.append("1. 定期清理 07-临时文件 目录中的过期内容")
        suggestions.append("2. 为 06-资源素材 建立更细分的分类")
        suggestions.append("3. 考虑为每个主要目录建立 README.md 说明文件")
        suggestions.append("4. 建立统一的文件命名规范文档")
        suggestions.append("5. 定期备份重要的工作文档和学习笔记")
        
        # 基于目录结构的建议
        if any("缺少" in warning for warning in self.warnings):
            suggestions.append("6. 补充缺失的目录结构以保持完整性")
        
        if any("命名不规范" in warning for warning in self.warnings):
            suggestions.append("7. 修复命名不规范的文件和目录")
        
        if any("过深" in suggestion for suggestion in self.suggestions):
            suggestions.append("8. 考虑简化过深的目录结构")
        
        self.suggestions.extend(suggestions)
    
    def _is_valid_naming(self, name: str) -> bool:
        """检查目录命名是否规范"""
        # 预期的目录格式: 数字前缀-中文名称
        if '-' in name and name.split('-')[0].isdigit():
            return True
        # 允许一些特殊情况
        allowed_names = ['.vscode', '__pycache__', 'git']
        return name in allowed_names
    
    def _is_valid_filename(self, name: str) -> bool:
        """检查文件名是否规范"""
        # 避免特殊字符
        invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
        return not any(char in name for char in invalid_chars)
    
    def _format_size(self, size_bytes: int) -> str:
        """格式化文件大小"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
    
    def generate_validation_report(self):
        """生成验证报告"""
        report = {
            "validation_summary": {
                "total_checks": len(self.validation_results),
                "warnings": len(self.warnings),
                "suggestions": len(self.suggestions)
            },
            "validation_results": self.validation_results,
            "warnings": self.warnings,
            "suggestions": self.suggestions
        }
        
        report_file = self.base_path / "结构验证报告.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report
    
    def run_validation(self):
        """执行完整的验证流程"""
        print("开始验证知识库目录结构...")
        print("=" * 50)
        
        try:
            # 1. 验证目录结构
            self.validate_directory_structure()
            print()
            
            # 2. 分析文件分布
            self.analyze_file_distribution()
            print()
            
            # 3. 检查命名一致性
            self.check_naming_consistency()
            print()
            
            # 4. 检查深度复杂度
            self.check_depth_complexity()
            print()
            
            # 5. 生成管理建议
            self.generate_management_suggestions()
            print()
            
            # 6. 生成报告
            report = self.generate_validation_report()
            
            # 打印结果
            print("=" * 50)
            print("验证完成!")
            print(f"验证项目: {report['validation_summary']['total_checks']}")
            print(f"警告数量: {report['validation_summary']['warnings']}")
            print(f"建议数量: {report['validation_summary']['suggestions']}")
            
            # 显示详细结果
            if self.validation_results:
                print("\n📊 验证结果:")
                for result in self.validation_results:
                    print(result)
            
            if self.warnings:
                print("\n⚠️ 警告信息:")
                for warning in self.warnings:
                    print(warning)
            
            if self.suggestions:
                print("\n💡 改进建议:")
                for suggestion in self.suggestions:
                    print(suggestion)
            
            print(f"\n详细报告已保存到: 结构验证报告.json")
            
        except Exception as e:
            print(f"验证过程中发生错误: {str(e)}")

def main():
    """主函数"""
    print("知识库目录结构验证工具")
    print("=" * 50)
    
    validator = KnowledgeBaseValidator()
    validator.run_validation()

if __name__ == "__main__":
    main()