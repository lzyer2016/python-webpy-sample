/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : auth

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2018-01-27 22:24:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `login_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `state` smallint(6) NOT NULL DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '张三', 'zhangsan', 'gyQIgEfxuSEX4Hm75U2HeA==', '1');
INSERT INTO `user` VALUES ('2', '李四', 'lisi', 'gyQIgEfxuSEX4Hm75U2HeA==', '1');
INSERT INTO `user` VALUES ('3', '王五', 'wangwu', 'gyQIgEfxuSEX4Hm75U2HeA==', '1');
