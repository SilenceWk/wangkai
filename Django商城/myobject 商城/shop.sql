/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.5.48-log : Database - shop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`shop` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `shop`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `detail` */

DROP TABLE IF EXISTS `detail`;

CREATE TABLE `detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `goodsid` int(11) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `detail` */

insert  into `detail`(`id`,`orderid`,`goodsid`,`name`,`price`,`num`) values (1,1,5,'数码相机',3000.00,1),(2,2,5,'数码相机',3000.00,1),(3,3,7,'电脑',9999.00,1),(4,3,10,'禁闭岛',0.00,3),(5,4,7,'电脑',9999.00,1),(6,4,10,'禁闭岛',0.00,3),(7,5,1,'手机',5999.00,1),(8,6,12,'钢铁侠',0.00,2),(17,19,13,'电视',123.00,1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-10-16 13:28:46'),(2,'auth','0001_initial','2017-10-16 13:28:46'),(3,'admin','0001_initial','2017-10-16 13:28:46'),(4,'admin','0002_logentry_remove_auto_add','2017-10-16 13:28:46'),(5,'contenttypes','0002_remove_content_type_name','2017-10-16 13:28:46'),(6,'auth','0002_alter_permission_name_max_length','2017-10-16 13:28:46'),(7,'auth','0003_alter_user_email_max_length','2017-10-16 13:28:46'),(8,'auth','0004_alter_user_username_opts','2017-10-16 13:28:46'),(9,'auth','0005_alter_user_last_login_null','2017-10-16 13:28:46'),(10,'auth','0006_require_contenttypes_0002','2017-10-16 13:28:46'),(11,'auth','0007_alter_validators_add_error_messages','2017-10-16 13:28:46'),(12,'auth','0008_alter_user_username_max_length','2017-10-16 13:28:46'),(13,'sessions','0001_initial','2017-10-16 13:28:46');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('8xqlps9ezggqfif9oxf17q4boh97umrg','ZTNkNTZhY2YwZWJjOTM1NTY4MDllMzg5MGU1M2U1N2M2YjljMDNlZjp7InZpcHVzZXIiOnsidXNlcm5hbWUiOiJmZnkiLCJuYW1lIjoiXHU3YjI2XHU5OGRlXHU3MWQ1IiwicGFzc3dvcmQiOiIyMDJjYjk2MmFjNTkwNzViOTY0YjA3MTUyZDIzNGI3MCIsInNleCI6MCwicGhvbmUiOiI5MTEiLCJjb2RlIjoiIiwiYWRkcmVzcyI6IiIsImVtYWlsIjoiZmZ5QHFxLmNvbSJ9LCJzaG9wbGlzdCI6e319','2017-11-02 14:25:28'),('betztkl8v4bmwr0sphr2c1vkvm0efj54','ZmY2ZTlkZDE0Yzg2NjYxNjFlYzllNTVhZTI1ODZjZDhiMWI1MTg2Zjp7InZpcHVzZXIiOnsidXNlcm5hbWUiOiJmZnkiLCJuYW1lIjoiXHU3YjI2XHU5OGRlXHU3MWQ1IiwicGFzc3dvcmQiOiIyMDJjYjk2MmFjNTkwNzViOTY0YjA3MTUyZDIzNGI3MCIsInNleCI6MCwicGhvbmUiOiI5MTEiLCJjb2RlIjoiIiwiYWRkcmVzcyI6IiIsImVtYWlsIjoiZmZ5QHFxLmNvbSJ9LCJzaG9wbGlzdCI6eyIxMCI6eyJpZCI6MTAsImdvb2RzIjoiXHU3OTgxXHU5NWVkXHU1YzliIiwicHJpY2UiOjAuMCwicGljbmFtZSI6IjE1MDg0NjMxNzMuODQyODIuanBnIiwibSI6NiwiZGVzY3IiOiIgICAgICAgICAgICAgICAgXHU1YzBmXHU2NzRlXHU1YjUwXHVmZjAxXHVmZjAxXHVmZjAxIn19fQ==','2017-11-04 10:48:44'),('jf2p380wurc5p2lt986qsp9h95ikuo6h','M2M4MTcxMWIzM2IzMjcxMjQ3YjkxMDI0OTNmZDYxZTY4ZjEzOTViOTp7InZpcHVzZXIiOnsiaWQiOjEsInVzZXJuYW1lIjoiYWRtaW4iLCJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6IjIwMmNiOTYyYWM1OTA3NWI5NjRiMDcxNTJkMjM0YjcwIiwic2V4IjowLCJwaG9uZSI6IjkxMSIsImNvZGUiOiIyMDAwMDAiLCJhZGRyZXNzIjoiXHU0ZTJkXHU1NmZkIiwiZW1haWwiOiJhZG1pbkBxcS5jb20ifSwidmVyaWZ5Y29kZSI6IkQ2OEEiLCJhZG1pbnVzZXIiOiJhZG1pbiJ9','2017-11-04 05:43:40'),('p2b5p0w9cnjh1xqnxfto2gflpkk2871c','YmFjYjVjOTAwMmIyMjVmZjNmNTk2YWMzNzFkM2M2MmJhZWZkYjdhZDp7InZlcmlmeWNvZGUiOiJPM0JaIn0=','2017-11-04 09:05:18'),('pz4ba48dayx0uddewng46gwfo1n4nd53','YTMyYTljNWIwYzMzYmZjZWYzNzdkODg4M2QzYWJmNzMzMzhhZWFkYzp7InZlcmlmeWNvZGUiOiJFSkgzIiwiYWRtaW51c2VyIjoiYWRtaW4ifQ==','2017-10-31 08:20:06'),('rn9t5pi9u06pjwhrbxpmznb1y8zn3s2g','NjUzM2JkYjhjYjcyNTdmNjgxZGFjOGVkNzNkZGZlNDkyZGIxNmM2ZDp7InZlcmlmeWNvZGUiOiIzOUhPIiwidXNlciI6eyJ1c2VybmFtZSI6ImFkbWluIiwibmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIyMDJjYjk2MmFjNTkwNzViOTY0YjA3MTUyZDIzNGI3MCIsInNleCI6MCwicGhvbmUiOiI5MTEiLCJjb2RlIjoiMjAwMDAwIiwiYWRkcmVzcyI6Ilx1NGUyZFx1NTZmZCIsImVtYWlsIjoiYWRtaW5AcXEuY29tIn0sInNob3AiOnsiaWQiOjIsImdvb2RzIjoiXHU3NTM3VFx1NjA2NCIsInByaWNlIjo5OTguMCwicGljbmFtZSI6IjE1MDgyMjA3MzYuNDEzNzk2Ny5qcGciLCJtIjowfSwic2hvcGxpc3QiOnsiMSI6eyJpZCI6MSwiZ29vZHMiOiJcdTYyNGJcdTY3M2EiLCJwcmljZSI6NTk5OS4wLCJwaWNuYW1lIjoiMTUwMTUyNjA0My43ODE0MzYuanBnIiwibSI6MSwiZGVzY3IiOiIifX0sImFkbWludXNlciI6ImFkbWluIiwidmlwdXNlciI6eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsIm5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiMjAyY2I5NjJhYzU5MDc1Yjk2NGIwNzE1MmQyMzRiNzAiLCJzZXgiOjAsInBob25lIjoiOTExIiwiY29kZSI6IjIwMDAwMCIsImFkZHJlc3MiOiJcdTRlMmRcdTU2ZmQiLCJlbWFpbCI6ImFkbWluQHFxLmNvbSJ9fQ==','2017-11-04 11:36:40'),('vqwqb8lgk6g0fyflqez78nooh361sxq3','ZWQ1NzNhNWNlNTg2MWU2MWIxOWM0NWY5NGI0ZTJhNGU1MmUzNDZjMDp7InZlcmlmeWNvZGUiOiJTS1RXIiwiYWRtaW51c2VyIjoiYWRtaW4ifQ==','2017-11-04 06:13:39'),('wgq1jb3lixxfttyv75znbwhmjb960n6i','MDVkYTM2MDIwMDIzNWQ3YTc2M2ZmYWMzMmNkMDU0ZTE2YjI0ZjY1OTp7InZpcHVzZXIiOnsiaWQiOjEsInVzZXJuYW1lIjoiYWRtaW4iLCJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6IjIwMmNiOTYyYWM1OTA3NWI5NjRiMDcxNTJkMjM0YjcwIiwic2V4IjowLCJwaG9uZSI6IjkxMSIsImNvZGUiOiIyMDAwMDAiLCJhZGRyZXNzIjoiXHU0ZTJkXHU1NmZkIiwiZW1haWwiOiJhZG1pbkBxcS5jb20ifSwic2hvcGxpc3QiOnsiMyI6eyJpZCI6MywiZ29vZHMiOiJcdThmZGVcdTg4NjNcdTg4ZDkiLCJwcmljZSI6Mzk5LjAsInBpY25hbWUiOiIxNTA4MjI3MzIwLjc2OTg5MjUuanBnIiwibSI6MSwiZGVzY3IiOiIgICAgICAgICAgICAgICAgXHU1OTA0XHU3NDA2XHU0ZTg2XHUzMDAyXHUzMDAyXHUzMDAyIn19LCJvcmRlcmxpc3QiOnsiMyI6eyJpZCI6MywiZ29vZHMiOiJcdThmZGVcdTg4NjNcdTg4ZDkiLCJwcmljZSI6Mzk5LjAsInBpY25hbWUiOiIxNTA4MjI3MzIwLjc2OTg5MjUuanBnIiwibSI6MSwiZGVzY3IiOiIgICAgICAgICAgICAgICAgXHU1OTA0XHU3NDA2XHU0ZTg2XHUzMDAyXHUzMDAyXHUzMDAyIn19LCJ0b3RhbCI6Mzk5LjB9','2017-11-03 15:22:35');

/*Table structure for table `goods` */

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) DEFAULT NULL,
  `goods` varchar(32) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` text,
  `price` double(6,2) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` tinyint(1) DEFAULT '1',
  `store` int(11) DEFAULT '0',
  `num` int(11) DEFAULT '0',
  `clicknum` int(11) DEFAULT '0',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_goods` (`typeid`),
  CONSTRAINT `FK_goods` FOREIGN KEY (`typeid`) REFERENCES `type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `goods` */

insert  into `goods`(`id`,`typeid`,`goods`,`company`,`descr`,`price`,`picname`,`state`,`store`,`num`,`clicknum`,`addtime`) values (1,10,'手机','苹果','',5999.00,'1501526043.781436.jpg',1,100,0,4,NULL),(2,3,'男T恤','江南皮革厂','                只要998.。。',998.00,'1508220736.4137967.jpg',1,1,0,2,1508220736),(3,8,'连衣裙','江南皮革厂','                处理了。。。',399.00,'1508227320.7698925.jpg',1,998,0,4,1508220812),(5,5,'数码相机','索尼','                大降价。。。',3000.00,'1508228188.3447683.jpg',2,10,0,28,1508221392),(6,4,'童装','江南皮革厂','                你想买吗？我不卖。。。',110.00,'1508232384.239057.jpg',1,0,0,3,1508232384),(7,9,'电脑','江南电子厂','                大降价....',9999.99,'1508232453.7945745.jpg',1,0,0,7,1508232453),(8,9,'电脑','江南电子厂','                不用了,谢谢...',9999.99,'1508232860.8122642.jpg',1,0,0,1,1508232860),(9,20,'金刚狼','美国','                金刚狼！！！',0.00,'1508463138.4768274.jpg',1,0,0,1,1508463138),(10,20,'禁闭岛','欧美','                小李子！！！',0.00,'1508463173.84282.jpg',1,0,0,3,1508463173),(11,20,'无人区','国产','                无人区！！！',0.00,'1508463205.1564429.jfif',1,0,0,0,1508463205),(12,20,'钢铁侠','欧美','                钢铁侠！！！',0.00,'1508463241.4842217.jfif',1,0,0,1,1508463241),(13,22,'电视','电视','                ',123.00,'1508574531.427912.jpg',1,1,0,1,1508574531);

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` int(11) DEFAULT NULL,
  `total` double(8,2) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `orders` */

insert  into `orders`(`id`,`uid`,`linkman`,`address`,`code`,`phone`,`addtime`,`total`,`status`) values (1,14,'符飞燕','天津市武清区','301700','911',1508510453,3000.00,0),(2,14,'符飞燕','天津市武清区','301700','911',1508510563,3000.00,0),(3,14,'符飞燕','天津市武清区','301700','911',1508510669,9999.00,1),(4,14,'符飞燕','天津市武清区','301700','911',1508510914,9999.00,3),(5,1,'admin','中国','200000','911',1508513841,5999.00,0),(6,14,'符飞燕','天津市武清区','301700','911',1508524870,0.00,0),(19,1,'admin','中国','200000','911',1508574715,123.00,0);

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

/*Data for the table `type` */

insert  into `type`(`id`,`name`,`pid`,`path`) values (1,'服装',0,'0,'),(2,'数码',0,'0,'),(3,'男装',1,'0,1,'),(4,'女装',1,'0,1,'),(5,'相机',2,'0,2,'),(6,'电脑',2,'0,2,'),(7,'西装',3,'0,1,3,'),(8,'连衣裙',4,'0,1,4,'),(9,'台式机',6,'0,2,6,'),(10,'笔记本',6,'0,2,6,'),(12,'男卫衣',3,'0,1,3,'),(15,'母婴',0,'0,'),(17,'儿童护理',15,'0,15,'),(19,'电影',0,'0,'),(20,'热销电影',19,'0,19,'),(21,'电子',0,'0,'),(22,'电视',21,'0,21,');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `password` char(32) NOT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `state` tinyint(1) DEFAULT '1',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `NewIndex1` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`name`,`password`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`) values (1,'admin','admin','202cb962ac59075b964b07152d234b70',0,'中国','200000','911','admin@qq.com',0,NULL),(2,'wangkai','王凯','202cb962ac59075b964b07152d234b70',1,'泰国','300450','110','wangkai@qq.com',1,1508154405),(3,'zedong','泽冬','202cb962ac59075b964b07152d234b70',1,'印度','120120','120','zedong@qq.com',2,NULL),(14,'ffy','符飞燕','202cb962ac59075b964b07152d234b70',0,'天津市武清区','301700','911','ffy@qq.com',0,NULL),(15,'mmd','么么哒','202cb962ac59075b964b07152d234b70',1,'','','110','mmd@qq.com',1,NULL),(25,'ds','大圣','202cb962ac59075b964b07152d234b70',1,'','','110','ds@qq.com',1,NULL),(26,'123','李娜','202cb962ac59075b964b07152d234b70',1,'','','123','123@qq.com',1,NULL),(42,'12','12','12',1,'','','12','12',1,NULL),(43,'jiangyan','姜妍','jy123456',1,'','','15122802380','399704129@qq.com',1,NULL),(45,'memeda','llll','e10adc3949ba59abbe56e057f20f883e',1,'','','13702150080','299704129@qq.com',1,NULL),(46,'wkwk','王凯','202cb962ac59075b964b07152d234b70',1,'123','123','111','wk@qq.com',1,1508574431),(48,'wwwwww','wwwwwww','0ad3f5f991400cb2f29e1ac9dc7533f0',1,'','','15122802380','wwwwwww@qq.com',1,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
