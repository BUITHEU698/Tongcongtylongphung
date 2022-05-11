-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 11, 2022 lúc 06:49 PM
-- Phiên bản máy phục vụ: 10.4.22-MariaDB
-- Phiên bản PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `thuoc_lao_long_phung`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app1_contactmodel`
--

CREATE TABLE `app1_contactmodel` (
  `id` bigint(20) NOT NULL,
  `username` varchar(25) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `app1_contactmodel`
--

INSERT INTO `app1_contactmodel` (`id`, `username`, `email`, `subject`, `message`) VALUES
(1, 'buitheu', '19522254@gm.uit.edu.vn', 'Tỏ Tình', 'dasdas');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app1_postblog`
--

CREATE TABLE `app1_postblog` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `body` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app2_portfoliomodel`
--

CREATE TABLE `app2_portfoliomodel` (
  `id` bigint(20) NOT NULL,
  `portfolioImg` varchar(100) NOT NULL,
  `portfolioBody` longtext NOT NULL,
  `portfolioName` varchar(200) NOT NULL,
  `portfolioPub` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `app2_portfoliomodel`
--

INSERT INTO `app2_portfoliomodel` (`id`, `portfolioImg`, `portfolioBody`, `portfolioName`, `portfolioPub`) VALUES
(1, '1', '1', '1', '1');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add site', 5, 'add_site'),
(18, 'Can change site', 5, 'change_site'),
(19, 'Can delete site', 5, 'delete_site'),
(20, 'Can view site', 5, 'view_site'),
(21, 'Can add content type', 6, 'add_contenttype'),
(22, 'Can change content type', 6, 'change_contenttype'),
(23, 'Can delete content type', 6, 'delete_contenttype'),
(24, 'Can view content type', 6, 'view_contenttype'),
(25, 'Can add session', 7, 'add_session'),
(26, 'Can change session', 7, 'change_session'),
(27, 'Can delete session', 7, 'delete_session'),
(28, 'Can view session', 7, 'view_session'),
(29, 'Can add contact model', 8, 'add_contactmodel'),
(30, 'Can change contact model', 8, 'change_contactmodel'),
(31, 'Can delete contact model', 8, 'delete_contactmodel'),
(32, 'Can view contact model', 8, 'view_contactmodel'),
(33, 'Can add post blog', 9, 'add_postblog'),
(34, 'Can change post blog', 9, 'change_postblog'),
(35, 'Can delete post blog', 9, 'delete_postblog'),
(36, 'Can view post blog', 9, 'view_postblog'),
(37, 'Can add portfolio model', 10, 'add_portfoliomodel'),
(38, 'Can change portfolio model', 10, 'change_portfoliomodel'),
(39, 'Can delete portfolio model', 10, 'delete_portfoliomodel'),
(40, 'Can view portfolio model', 10, 'view_portfoliomodel');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$uLr7umh1bkyXPjtlpXl7R5$JhWv/POacI5WpVM1Z7xf+lmX7lnENu5axlZGQu8lXdE=', '2022-05-10 19:01:08.182809', 1, 'buitheu', '', '', '19522254@ms.uit.edu.vn', 1, 1, '2022-05-10 17:03:20.259941');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-05-10 17:55:38.563156', '1', 'qaefrewaf', 1, '[{\"added\": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'app1', 'contactmodel'),
(9, 'app1', 'postblog'),
(10, 'app2', 'portfoliomodel'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(6, 'contenttypes', 'contenttype'),
(7, 'sessions', 'session'),
(5, 'sites', 'site');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-10 17:00:23.849748'),
(2, 'auth', '0001_initial', '2022-05-10 17:00:24.369494'),
(3, 'admin', '0001_initial', '2022-05-10 17:00:24.488692'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-10 17:00:24.501680'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-10 17:00:24.511672'),
(6, 'app1', '0001_initial', '2022-05-10 17:00:24.540645'),
(7, 'app1', '0002_rename_usename_contacform_username', '2022-05-10 17:00:24.556629'),
(8, 'app1', '0003_rename_contacform_contactmodel', '2022-05-10 17:00:24.581606'),
(9, 'app1', '0004_rename_contactmodel_contactform', '2022-05-10 17:00:24.605583'),
(10, 'app1', '0005_rename_contactform_contactmodel', '2022-05-10 17:00:24.630564'),
(11, 'app1', '0006_possform', '2022-05-10 17:00:24.654538'),
(12, 'app1', '0007_rename_possform_postblog', '2022-05-10 17:00:24.679779'),
(13, 'app2', '0001_initial', '2022-05-10 17:00:24.709753'),
(14, 'contenttypes', '0002_remove_content_type_name', '2022-05-10 17:00:24.829317'),
(15, 'auth', '0002_alter_permission_name_max_length', '2022-05-10 17:00:24.878269'),
(16, 'auth', '0003_alter_user_email_max_length', '2022-05-10 17:00:24.901245'),
(17, 'auth', '0004_alter_user_username_opts', '2022-05-10 17:00:24.914234'),
(18, 'auth', '0005_alter_user_last_login_null', '2022-05-10 17:00:24.981067'),
(19, 'auth', '0006_require_contenttypes_0002', '2022-05-10 17:00:24.998051'),
(20, 'auth', '0007_alter_validators_add_error_messages', '2022-05-10 17:00:25.012036'),
(21, 'auth', '0008_alter_user_username_max_length', '2022-05-10 17:00:25.041011'),
(22, 'auth', '0009_alter_user_last_name_max_length', '2022-05-10 17:00:25.070983'),
(23, 'auth', '0010_alter_group_name_max_length', '2022-05-10 17:00:25.107948'),
(24, 'auth', '0011_update_proxy_permissions', '2022-05-10 17:00:25.131926'),
(25, 'auth', '0012_alter_user_first_name_max_length', '2022-05-10 17:00:25.198864'),
(26, 'sessions', '0001_initial', '2022-05-10 17:00:25.259806'),
(27, 'sites', '0001_initial', '2022-05-10 17:00:25.303766'),
(28, 'sites', '0002_alter_domain_unique', '2022-05-10 17:00:25.327744'),
(29, 'app2', '0002_portfoliomodel_portfoliopub', '2022-05-10 17:46:43.749174'),
(30, 'app2', '0003_alter_portfoliomodel_portfoliopub', '2022-05-10 17:51:10.245667'),
(31, 'app2', '0004_alter_portfoliomodel_portfoliopub', '2022-05-11 16:45:49.036740'),
(32, 'app2', '0005_auto_20220511_1414', '2022-05-11 16:45:49.419382'),
(33, 'app2', '0006_auto_20220511_1417', '2022-05-11 16:45:49.648170'),
(34, 'app2', '0007_alter_portfoliomodel_portfoliotimepub', '2022-05-11 16:45:49.669151'),
(35, 'app2', '0008_auto_20220511_1421', '2022-05-11 16:45:49.720104'),
(36, 'app2', '0009_auto_20220511_1750', '2022-05-11 16:45:49.859973'),
(37, 'app2', '0010_auto_20220511_1822', '2022-05-11 16:45:50.092757'),
(38, 'app2', '0011_portfoliomodel_portfoliobody', '2022-05-11 16:45:50.259601'),
(39, 'app2', '0012_portfoliomodel_portfoliopub', '2022-05-11 16:45:50.356512'),
(40, 'app2', '0013_portfoliomodel_portfoliotimepub', '2022-05-11 16:45:50.452420'),
(41, 'app2', '0014_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.533345'),
(42, 'app2', '0015_remove_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.582302'),
(43, 'app2', '0016_alter_portfoliomodel_portfoliotimepub', '2022-05-11 16:45:50.599287'),
(44, 'app2', '0017_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.676215'),
(45, 'app2', '0018_remove_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.725167'),
(46, 'app2', '0019_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.806092'),
(47, 'app2', '0020_alter_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.822077'),
(48, 'app2', '0021_remove_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.870032'),
(49, 'app2', '0022_portfoliomodel_portfolioimg', '2022-05-11 16:45:50.953956'),
(50, 'app2', '0023_auto_20220511_2229', '2022-05-11 16:45:51.108810');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('xxgbg2tglf9ui8exgvyiwgu0q1qjba4i', '.eJxVjEEOwiAQRe_C2pApFOi4dO8ZyMCMUjU0Ke3KeHfbpAvd_vfef6tI61Li2mSOI6uz6tTpd0uUn1J3wA-q90nnqS7zmPSu6IM2fZ1YXpfD_Tso1MpWAydkBiAmCeQcGptcn0wOBi0KoxXIoQMPvUlh8MFs8iAWA9HNZ1CfL-bpN5U:1noV6a:ddJhEsEE0U5kkPqxhLzVkwAhCO8Y1fLiKH9eWfo0ICg', '2022-05-24 19:01:08.187804');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `app1_contactmodel`
--
ALTER TABLE `app1_contactmodel`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app1_postblog`
--
ALTER TABLE `app1_postblog`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app2_portfoliomodel`
--
ALTER TABLE `app2_portfoliomodel`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Chỉ mục cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Chỉ mục cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Chỉ mục cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Chỉ mục cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Chỉ mục cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Chỉ mục cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Chỉ mục cho bảng `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `app1_contactmodel`
--
ALTER TABLE `app1_contactmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `app1_postblog`
--
ALTER TABLE `app1_postblog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app2_portfoliomodel`
--
ALTER TABLE `app2_portfoliomodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT cho bảng `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Các ràng buộc cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Các ràng buộc cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Các ràng buộc cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Các ràng buộc cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
