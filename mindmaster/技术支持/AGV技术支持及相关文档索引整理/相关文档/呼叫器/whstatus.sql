/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : wh

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-04-29 09:25:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `whstatus`
-- ----------------------------
DROP TABLE IF EXISTS `whstatus`;
CREATE TABLE `whstatus` (
  `LINE` varchar(64) NOT NULL,
  `LED1` varchar(64) DEFAULT '0',
  `LED2` varchar(64) DEFAULT '0',
  `LED3` varchar(64) DEFAULT '0',
  `LED4` varchar(64) DEFAULT '0',
  `LED5` varchar(64) DEFAULT '0',
  `LED6` varchar(64) DEFAULT '0',
  `LED7` varchar(64) DEFAULT '0',
  `LED8` varchar(64) DEFAULT '0',
  `LED9` varchar(64) DEFAULT '0',
  `LED10` varchar(64) DEFAULT '0',
  `LED11` varchar(64) DEFAULT '0',
  `LED12` varchar(64) DEFAULT '0',
  `STATUS` varchar(64) DEFAULT NULL,
  `ATTR1` varchar(64) DEFAULT '',
  `ATTR2` varchar(64) DEFAULT '',
  `ATTR3` varchar(64) DEFAULT '',
  `ATTR4` varchar(64) DEFAULT NULL,
  `ATTR5` varchar(64) DEFAULT '',
  `ATTR6` varchar(64) DEFAULT '',
  `created_at` int(11) DEFAULT NULL,
  `updated_at` int(11) DEFAULT NULL,
  PRIMARY KEY (`LINE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of whstatus
-- ----------------------------
INSERT INTO `whstatus` VALUES ('L001', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L002', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L003', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L004', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L005', '3', '2', '3', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L006', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L007', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L008', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L009', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L010', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
INSERT INTO `whstatus` VALUES ('L011', '0', '0', '0', '0', '0', '0', null, '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '0', '0');
