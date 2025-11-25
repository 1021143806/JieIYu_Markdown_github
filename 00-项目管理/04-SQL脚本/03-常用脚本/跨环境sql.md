# 跨环境SQL





## 任务模板插入空白

### 跨环境任务模板

```sql
INSERT INTO `wms`.`fy_cross_model_process`(`model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES ( NULL, NULL, 1, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process`(`model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES ( NULL, NULL, 1, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process`(`model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES ( NULL, NULL, 1, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process`(`model_process_code`, `model_process_name`, `enable`, `request_url`, `create_time`, `capacity`, `target_points`, `area_id`, `target_points_ip`, `update_time`, `backflow_template_code`, `comeback_template_code`, `change_charge_template_code`, `min_power`, `back_wait_time`, `check_area_name`) VALUES ( NULL, NULL, 1, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL);
```

### 跨环境子任务

```sql
INSERT INTO `wms`.`fy_cross_model_process_detail`( `model_process_id`, `task_seq`, `task_servicec`, `template_code`, `template_name`, `task_path`, `backflow_template_code`, `comeback_template_code`, `back_wait_time`) VALUES ( 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process_detail`( `model_process_id`, `task_seq`, `task_servicec`, `template_code`, `template_name`, `task_path`, `backflow_template_code`, `comeback_template_code`, `back_wait_time`) VALUES ( 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process_detail`( `model_process_id`, `task_seq`, `task_servicec`, `template_code`, `template_name`, `task_path`, `backflow_template_code`, `comeback_template_code`, `back_wait_time`) VALUES ( 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `wms`.`fy_cross_model_process_detail`( `model_process_id`, `task_seq`, `task_servicec`, `template_code`, `template_name`, `task_path`, `backflow_template_code`, `comeback_template_code`, `back_wait_time`) VALUES ( 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
```

