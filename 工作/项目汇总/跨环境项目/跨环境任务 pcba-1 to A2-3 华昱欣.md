

# 跨环境任务 pcba-1 to A2-3 华昱欣

## 路线梳理

2.31 25 区域 电装 1F

![image-20241018084952908](C:\git\JieIYu_Markdown_1\工作\跨环境任务 pcba-1 to A3-3 华昱欣.assets\image-20241018084952908.png)

2.31 2 区域 富阳电装工厂

2.32 3 区域 A3 结构备料部连廊

2.17 1 区域 A2 备料 and 存储二部

2.19 4 区域 二楼 -> 3 区域华昱欣

![image-20241018085452549](C:\git\JieIYu_Markdown_1\工作\跨环境任务 pcba-1 to A3-3 华昱欣.assets\image-20241018085452549.png)

 

## 细节

- 2.31 25 区域 电装 1F
  - 同239 - 3-5
  - ![image-20241018091931891](C:\git\JieIYu_Markdown_1\工作\跨环境任务 pcba-1 to A2-3 华昱欣.assets\image-20241018091931891.png)

![image-20241018084952908](C:\git\JieIYu_Markdown_1\工作\跨环境任务 pcba-1 to A3-3 华昱欣.assets\image-20241018084952908.png)

- 2.31 2 区域 富阳电装工厂
  - 239-6

- 2.32 3 区域 A3 结构备料部连廊
  - 239-7
  - 目标点 55310282 去 2.17

- 2.17 1 区域 A2 备料 and 存储二部

- 2.19 4 区域 二楼 -> 3 区域华昱欣

![image-20241018085452549](C:\git\JieIYu_Markdown_1\工作\跨环境任务 pcba-1 to A3-3 华昱欣.assets\image-20241018085452549.png)

- 空车返回

  - K_31A1DZ1F_to_19A2HYX3F_go
    - 空车A1pcba1F去A2华昱欣3F
    - 2.19-1 -> 2.17-1 -> 2.32-3 -> 2.31-2 -> 2.31-25
  - K_31A1DZ1F_to_19A2HYX3F_leave
    - 空车A1pcba1F去A2华昱欣3F回
    - 2.31-25-> 2.31-2 -> 2.32-3 -> 2.17-1 -> 2.19-1

- sql

  - 主任务模板

  ```sql
  INSERT INTO `wms`.`fy_cross_model_process`(`id`, `model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES (246, 'K_31A1DZ1F_to_19A2HYX3F_go', '空车A1pcba1F去A2华昱欣3F', 1, 'http://127.0.0.1:7000/ics/taskOrder/updateStatus', '2023-06-14 22:44:50', 0, NULL, 1, 'http://10.68.2.17:7000', '2023-06-14 22:44:54', NULL, NULL, NULL, NULL, NULL, '');
  INSERT INTO `wms`.`fy_cross_model_process`(`id`, `model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES (247, 'K_31A1DZ1F_to_19A2HYX3F_leave', '空车A1pcba1F去A2华昱欣3F回', 1, 'http://127.0.0.1:7000/ics/taskOrder/updateStatus', '2023-06-14 22:44:50', 0, NULL, 1, 'http://10.68.2.17:7000', '2023-06-14 22:44:54', NULL, NULL, NULL, NULL, NULL, '');
  
  ```

  - 子任务模板

  ```sql
  
  ```

  

