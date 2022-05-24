-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 20, 2022 lúc 07:09 AM
-- Phiên bản máy phục vụ: 10.4.22-MariaDB
-- Phiên bản PHP: 8.0.13

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
-- Cấu trúc bảng cho bảng `app1_cartitemmodel`
--

CREATE TABLE `app1_cartitemmodel` (
  `id` bigint(20) NOT NULL,
  `quantile` int(11) NOT NULL,
  `cart_id` bigint(20) NOT NULL,
  `products_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app1_cartmodel`
--

CREATE TABLE `app1_cartmodel` (
  `id` bigint(20) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app1_ordermodel`
--

CREATE TABLE `app1_ordermodel` (
  `id` bigint(20) NOT NULL,
  `ShipAddress` varchar(255) NOT NULL,
  `order_description` longtext NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `cart_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Cấu trúc bảng cho bảng `app1_usermodel`
--

CREATE TABLE `app1_usermodel` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phoneNumber` varchar(11) NOT NULL,
  `userName` varchar(25) NOT NULL,
  `password` varchar(30) NOT NULL,
  `resetpassword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app2_portfoliomodel`
--

CREATE TABLE `app2_portfoliomodel` (
  `id` bigint(20) NOT NULL,
  `portfolioName` varchar(200) NOT NULL,
  `portfolioTimePub` datetime(6) NOT NULL,
  `portfolioBody` longtext NOT NULL,
  `portfolioImg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `app2_portfoliomodel`
--

INSERT INTO `app2_portfoliomodel` (`id`, `portfolioName`, `portfolioTimePub`, `portfolioBody`, `portfolioImg`) VALUES
(1, 'Điếu cày', '2022-05-20 11:44:00.000000', 'chất liệu được làm từ nhiều loại khác nhau như: tre, trúc, inox. Kích thước đa dạng: 20cm, 35cm, 45cm, 60cm, 80cm. Nhận làm các điếu cày theo yêu cầu', 'danhmuc1_4SBSUqp.jpg'),
(2, 'Nỏ điếu cày', '2022-05-20 11:45:00.000000', 'Hay còn gọi là phiểu, nhiều loại chất liệu khác nhau như gỗ các loại cây, inox,…', 'danhmuc2_T4h7F8s.jpg'),
(3, 'Thuốc lào', '2022-05-20 11:45:00.000000', 'Nhiều loại thuốc lào khác nhau theo các tỉnh phía Bắc. Thuốc lào Thanh Hóa, thuốc lào Nghệ An, thuốc lào Hải Phòng,… Theo nhiều cấp độ giúp Lào thủ có những phút giây trải nghiệm thú vị', 'danhmuc3_33V57ld.jpg');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app2_productsmodel`
--

CREATE TABLE `app2_productsmodel` (
  `id` bigint(20) NOT NULL,
  `productsName` varchar(200) NOT NULL,
  `productsBody` longtext NOT NULL,
  `productsImg` varchar(100) NOT NULL,
  `productsPrice` double NOT NULL,
  `productsPriceOther` double NOT NULL,
  `productsTimePub` datetime(6) NOT NULL,
  `weight` double NOT NULL,
  `inventory` double NOT NULL,
  `portfolioModel_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `app2_productsmodel`
--

INSERT INTO `app2_productsmodel` (`id`, `productsName`, `productsBody`, `productsImg`, `productsPrice`, `productsPriceOther`, `productsTimePub`, `weight`, `inventory`, `portfolioModel_id`) VALUES
(1, 'Điếu cày inox 20cm', 'Được phủ bên ngoài lớp inox không ghỉ, bên trong là ống tre.', 'sanpham1_isODaVK.png', 45000, 55000, '2022-05-20 11:46:00.000000', 500, 29, 1),
(2, 'Điếu cày inox 35cm', 'Được phủ bên ngoài lớp inox không ghỉ, bên trong là ống tre.', 'sanpham1_wj1kUQw.png', 70000, 75000, '2022-05-20 11:47:00.000000', 550, 15, 1),
(3, 'Điếu cày inox 45cm', 'Được phủ bên ngoài lớp inox không ghỉ, bên trong là ống tre.', 'sanpham1_Pw90Fey.png', 80000, 85000, '2022-05-20 11:49:00.000000', 600, 30, 1),
(4, 'Điếu cày inox 60cm', 'Được phủ bên ngoài lớp inox không ghỉ, bên trong là ống tre.', 'sanpham1_yjjKEpL.png', 85000, 95000, '2022-05-20 11:50:00.000000', 610, 21, 1),
(5, 'Điếu cày inox 80cm', 'Được phủ bên ngoài lớp inox không ghỉ, bên trong là ống tre.', 'sanpham1_fe44Ss0.png', 90000, 102000, '2022-05-20 11:51:00.000000', 700, 11, 1),
(6, 'Điếu cày tre 20cm', 'Làm hoàn từ tre không họa tiết', 'sanpham2_pwpVKX2.jpeg', 31000, 35000, '2022-05-20 11:51:00.000000', 500, 105, 1),
(7, 'Điếu cày tre 35cm', 'Làm hoàn từ tre không họa tiết', 'sanpham2_IXJnedn.jpeg', 45000, 49000, '2022-05-20 11:52:00.000000', 580, 97, 1),
(8, 'Điếu cày tre 45cm', 'Làm hoàn từ tre không họa tiết', 'sanpham2_uNDXs5d.jpeg', 50000, 52000, '2022-05-20 11:52:00.000000', 610, 68, 1),
(9, 'Điếu cày tre 60cm', 'Làm hoàn từ tre không họa tiết', 'sanpham2_oeYXwAF.jpeg', 58000, 70000, '2022-05-20 11:53:00.000000', 660, 49, 1),
(10, 'Điếu cày tre 80cm', 'Làm hoàn từ tre không họa tiết', 'sanpham2_yujcv5y.jpeg', 70000, 80000, '2022-05-20 11:53:00.000000', 700, 36, 1),
(11, 'Điếu cày trúc 20cm', 'Làm hoàn từ trúc, có họa tiết, có khắc rồng phượng đẹp mắt', 'sanpham3_8M9dCgq.jpg', 45000, 60000, '2022-05-20 11:54:00.000000', 400, 25, 1),
(12, 'Điếu cày trúc 35cm', 'Làm hoàn từ trúc, có họa tiết, có khắc rồng phượng đẹp mắt', 'sanpham3_TPkFt82.jpg', 65000, 75000, '2022-05-20 11:54:00.000000', 450, 34, 1),
(13, 'Điếu cày trúc 45cm', 'Làm hoàn từ trúc, có họa tiết, có khắc rồng phượng đẹp mắt', 'sanpham3_0veWNaW.jpg', 79000, 85000, '2022-05-20 11:55:00.000000', 510, 12, 1),
(14, 'Điếu cày trúc 60cm', 'Làm hoàn từ trúc, có họa tiết, có khắc rồng phượng đẹp mắt', 'sanpham3_92vDefo.jpg', 90000, 105000, '2022-05-20 11:55:00.000000', 570, 31, 1),
(15, 'Điếu cày trúc 80cm', 'Làm hoàn từ trúc, có họa tiết, có khắc rồng phượng đẹp mắt', 'sanpham3_IxjKSnj.jpg', 120000, 135000, '2022-05-20 11:56:00.000000', 600, 45, 1),
(16, 'Nỏ inox', 'Làm hoàn toàn từ chất liệu inox đúc', 'nodieu1_uV8k1jA.jpg', 17000, 20000, '2022-05-20 11:57:00.000000', 20, 109, 2),
(17, 'Nỏ tre', 'Làm hoàn toàn từ chất liệu cây tre. Phía trên miệng phiểu hình tròn làm từ gỗ cây', 'nodieu2_FJwxVQR.jpg', 28000, 30000, '2022-05-20 11:57:00.000000', 10, 132, 2),
(18, 'Nỏ trúc', 'Làm hoàn toàn từ chất liệu cây trúc. Phía trên miệng phiểu bọc lớp đồng sang trọng bắt mắt', 'nodieu3_pzkVAbf.jpg', 31000, 35000, '2022-05-20 11:58:00.000000', 10, 79, 2),
(19, 'Thuốc lào Thanh Hóa loại 1', 'Nguồn gốc xuất sứ từ tỉnh Thanh hóa. Loại 1 khá nhẹ dành cho các lào thủ tập chơi', 'thuoclao1_ltkTrZs.jpg', 47000, 50000, '2022-05-20 11:58:00.000000', 100, 100, 3),
(20, 'Thuốc lào Thanh Hóa loại 2', 'Nguồn gốc xuất sứ từ tỉnh Thanh hóa. Loại 2 tầm trung dành cho các lào thủ chơi đã lâu', 'thuoclao1_cXhwSSa.jpg', 55000, 62000, '2022-05-20 11:59:00.000000', 100, 100, 3),
(21, 'Thuốc lào Thanh Hóa loại 3', 'Nguồn gốc xuất sứ từ tỉnh Thanh hóa. Loại 3 siêu siêu phê và say khi hút nên có người bên cạnh để hãm phê', 'thuoclao1_zApnVTH.jpg', 65000, 70000, '2022-05-20 12:00:00.000000', 100, 100, 3),
(22, 'Thuốc lào Nghệ An loại 1', 'Nguồn gốc xuất sứ từ tỉnh Nghệ an. Loại 1 khá nhẹ ít khét dành cho các lào thủ tập chơi', 'thuoclao2_RYYxUo4.jpg', 49000, 50000, '2022-05-20 12:02:00.000000', 100, 100, 3),
(23, 'Thuốc lào Nghệ An loại 2', 'Nguồn gốc xuất sứ từ tỉnh Nghệ an. Loại 2 mạnh người chơi lâu cũng có thể say từ 10-15s', 'thuoclao2_vPze0za.jpg', 60000, 62000, '2022-05-20 12:02:00.000000', 100, 100, 3),
(24, 'Thuốc lào Nghệ An loại 3', 'Nguồn gốc xuất sứ từ tỉnh Nghệ an. Loại 3 mạnh người chơi lần đầu nên chú ý không là say lắm đấy', 'thuoclao2_RDYdmsI.jpg', 67000, 70000, '2022-05-20 12:03:00.000000', 100, 100, 3),
(25, 'Thuốc lào Hải Phòng loại 1', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng. Loại 1 khá êm không khét dành cho các lào thủ tập chơi', 'thuoclao3_VGlgK0h.png', 45000, 50000, '2022-05-20 12:05:00.000000', 100, 100, 3),
(26, 'Thuốc lào Hải Phòng loại 2', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng. Loại 2 êm diệu phê từ từ 10-15s', 'thuoclao3_P5FBNmJ.png', 48000, 57000, '2022-05-20 12:06:00.000000', 100, 100, 3),
(27, 'Thuốc lào Hải Phòng loại 3', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng. Loại 3 không phê mạnh bằng thanh hóa nhưng thời gian phê rất lâu', 'thuoclao3_GWJEE0e.png', 58000, 64000, '2022-05-20 12:06:00.000000', 100, 100, 3),
(28, 'Thuốc lào Tiên Lãng loại 1', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng, là 1 thương hiệu thuốc lào nổi tiếng. Loại 1 khá nhẹ dành cho các lào thủ tập chơi', 'thuoclao4_0SleNTm.jpg', 63000, 70000, '2022-05-20 12:07:00.000000', 100, 100, 3),
(29, 'Thuốc lào Tiên Lãng loại 2', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng, là 1 thương hiệu thuốc lào nổi tiếng. Loại 2 thơm ngon, không bị khét', 'thuoclao4_BrfJEN6.jpg', 80000, 85000, '2022-05-20 12:07:00.000000', 100, 100, 3),
(30, 'Thuốc lào Tiên Lãng loại 3', 'Nguồn gốc xuất sứ từ tỉnh Hải Phòng, là 1 thương hiệu thuốc lào nổi tiếng. Loại 3 mạnh nhất trong các loại thuốc lào', 'thuoclao4_hSs821O.jpg', 99000, 103000, '2022-05-20 12:08:00.000000', 100, 100, 3);

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
(37, 'Can add user model', 10, 'add_usermodel'),
(38, 'Can change user model', 10, 'change_usermodel'),
(39, 'Can delete user model', 10, 'delete_usermodel'),
(40, 'Can view user model', 10, 'view_usermodel'),
(41, 'Can add cart model', 11, 'add_cartmodel'),
(42, 'Can change cart model', 11, 'change_cartmodel'),
(43, 'Can delete cart model', 11, 'delete_cartmodel'),
(44, 'Can view cart model', 11, 'view_cartmodel'),
(45, 'Can add order model', 12, 'add_ordermodel'),
(46, 'Can change order model', 12, 'change_ordermodel'),
(47, 'Can delete order model', 12, 'delete_ordermodel'),
(48, 'Can view order model', 12, 'view_ordermodel'),
(49, 'Can add cart item model', 13, 'add_cartitemmodel'),
(50, 'Can change cart item model', 13, 'change_cartitemmodel'),
(51, 'Can delete cart item model', 13, 'delete_cartitemmodel'),
(52, 'Can view cart item model', 13, 'view_cartitemmodel'),
(53, 'Can add portfolio model', 14, 'add_portfoliomodel'),
(54, 'Can change portfolio model', 14, 'change_portfoliomodel'),
(55, 'Can delete portfolio model', 14, 'delete_portfoliomodel'),
(56, 'Can view portfolio model', 14, 'view_portfoliomodel'),
(57, 'Can add products model', 15, 'add_productsmodel'),
(58, 'Can change products model', 15, 'change_productsmodel'),
(59, 'Can delete products model', 15, 'delete_productsmodel'),
(60, 'Can view products model', 15, 'view_productsmodel');

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
(1, 'pbkdf2_sha256$260000$TLZcvwmwBRYCRba7mCRhoe$BEHWn2jV+Nz5SbC9SYvC7GMayoGVbNRYS9jJ+y75XLs=', '2022-05-19 09:27:04.235378', 1, 'minhphung', '', '', 'minhphung@gmail.com', 1, 1, '2022-05-19 09:25:07.539238'),
(2, 'pbkdf2_sha256$260000$FQvbbaBJHUdAEiJLIyypCr$so/TaaHNX7EQxCNj2Z6fgGYwYOuf1txtUIe8rGdNXI8=', '2022-05-20 04:43:57.796748', 1, 'nhom1', '', '', '123@gmail.com', 1, 1, '2022-05-20 04:43:25.387959');

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
(13, 'app1', 'cartitemmodel'),
(11, 'app1', 'cartmodel'),
(8, 'app1', 'contactmodel'),
(12, 'app1', 'ordermodel'),
(9, 'app1', 'postblog'),
(10, 'app1', 'usermodel'),
(14, 'app2', 'portfoliomodel'),
(15, 'app2', 'productsmodel'),
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
(1, 'contenttypes', '0001_initial', '2022-05-19 09:24:21.892333'),
(2, 'auth', '0001_initial', '2022-05-19 09:24:23.485288'),
(3, 'admin', '0001_initial', '2022-05-19 09:24:23.785329'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-19 09:24:23.799288'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-19 09:24:23.816288'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-19 09:24:23.938288'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-19 09:24:24.062288'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-19 09:24:24.131288'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-19 09:24:24.150291'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-19 09:24:24.255291'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-19 09:24:24.263290'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-19 09:24:24.280288'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-19 09:24:24.311288'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-19 09:24:24.342299'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-19 09:24:24.373292'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-19 09:24:24.391291'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-19 09:24:24.424289'),
(18, 'app2', '0001_initial', '2022-05-19 09:24:24.480288'),
(19, 'app2', '0002_portfoliomodel_portfoliopub', '2022-05-19 09:24:24.519289'),
(20, 'app2', '0003_alter_portfoliomodel_portfoliopub', '2022-05-19 09:24:24.528349'),
(21, 'app2', '0004_alter_portfoliomodel_portfoliopub', '2022-05-19 09:24:24.538314'),
(22, 'app2', '0005_auto_20220511_1414', '2022-05-19 09:24:24.689288'),
(23, 'app2', '0006_auto_20220511_1417', '2022-05-19 09:24:24.823288'),
(24, 'app2', '0007_alter_portfoliomodel_portfoliotimepub', '2022-05-19 09:24:24.832289'),
(25, 'app2', '0008_auto_20220511_1421', '2022-05-19 09:24:24.849318'),
(26, 'app2', '0009_auto_20220512_0044', '2022-05-19 09:24:24.861290'),
(27, 'app2', '0010_productsmodel', '2022-05-19 09:24:25.036331'),
(28, 'app2', '0011_auto_20220512_0215', '2022-05-19 09:24:25.093307'),
(29, 'app1', '0001_initial', '2022-05-19 09:24:25.293288'),
(30, 'app1', '0002_rename_usename_contacform_username', '2022-05-19 09:24:25.332289'),
(31, 'app1', '0003_rename_contacform_contactmodel', '2022-05-19 09:24:25.382290'),
(32, 'app1', '0004_rename_contactmodel_contactform', '2022-05-19 09:24:25.426288'),
(33, 'app1', '0005_rename_contactform_contactmodel', '2022-05-19 09:24:25.470291'),
(34, 'app1', '0006_possform', '2022-05-19 09:24:25.531331'),
(35, 'app1', '0007_rename_possform_postblog', '2022-05-19 09:24:25.576292'),
(36, 'app1', '0008_cartitemmodel_cartmodel_ordermodel_usermodel', '2022-05-19 09:24:27.132336'),
(37, 'app1', '0009_auto_20220512_0301', '2022-05-19 09:24:28.193288'),
(38, 'app1', '0010_auto_20220513_0344', '2022-05-19 09:24:28.418330'),
(39, 'app1', '0011_auto_20220513_0347', '2022-05-19 09:24:28.461290'),
(40, 'app1', '0012_auto_20220513_0349', '2022-05-19 09:24:28.477289'),
(41, 'app1', '0013_alter_usermodel_username', '2022-05-19 09:24:28.489290'),
(42, 'app1', '0014_alter_usermodel_username', '2022-05-19 09:24:28.502289'),
(43, 'app2', '0012_auto_20220512_0446', '2022-05-19 09:24:28.519289'),
(44, 'app2', '0013_remove_productsmodel_portfoliomodel', '2022-05-19 09:24:28.589289'),
(45, 'app2', '0014_productsmodel_portfoliomodel', '2022-05-19 09:24:28.746289'),
(46, 'app2', '0015_alter_productsmodel_weight', '2022-05-19 09:24:28.759289'),
(47, 'app2', '0016_auto_20220513_1200', '2022-05-19 09:24:29.117288'),
(48, 'app2', '0017_alter_productsmodel_productstimepub', '2022-05-19 09:24:29.128316'),
(49, 'app2', '0018_remove_productsmodel_productspub', '2022-05-19 09:24:29.197330'),
(50, 'app2', '0019_remove_portfoliomodel_portfoliopub_and_more', '2022-05-19 09:24:29.226289'),
(51, 'sessions', '0001_initial', '2022-05-19 09:24:29.318289'),
(52, 'sites', '0001_initial', '2022-05-19 09:24:29.410287'),
(53, 'sites', '0002_alter_domain_unique', '2022-05-19 09:24:29.474352');

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
('19wd6uo7emkya6jopgzwk7zj5f3servq', '.eJxVjDsOwjAQBe_iGlms8ZeSPmewdu01DiBHipMKcXcSKQW0b-bNW0RclxrXznMcs7gKJU6_G2F6cttBfmC7TzJNbZlHkrsiD9rlMGV-3Q73L1Cx1-19MUZbHYKFkhQzWmJQDooFBnCYFRY0xtvgjHae81YOGpQmS-iBzuLzBdHRN6M:1nruUX:g7rK8e6gvz4Op2TMZa5Uys1tINK6tPHs1-kQ-Hn82So', '2022-06-03 04:43:57.812746');

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
-- Chỉ mục cho bảng `app1_cartitemmodel`
--
ALTER TABLE `app1_cartitemmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_cartitemmodel_cart_id_c8389927_fk_app1_cartmodel_id` (`cart_id`),
  ADD KEY `app1_cartitemmodel_products_id_2b50f5f3_fk_app2_productsmodel_id` (`products_id`);

--
-- Chỉ mục cho bảng `app1_cartmodel`
--
ALTER TABLE `app1_cartmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_cartmodel_user_id_9bf23b63_fk_app1_usermodel_id` (`user_id`);

--
-- Chỉ mục cho bảng `app1_contactmodel`
--
ALTER TABLE `app1_contactmodel`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app1_ordermodel`
--
ALTER TABLE `app1_ordermodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app1_ordermodel_cart_id_63c474c4_fk_app1_cartmodel_id` (`cart_id`),
  ADD KEY `app1_ordermodel_user_id_4ae29bdf_fk_app1_usermodel_id` (`user_id`);

--
-- Chỉ mục cho bảng `app1_postblog`
--
ALTER TABLE `app1_postblog`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app1_usermodel`
--
ALTER TABLE `app1_usermodel`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app2_portfoliomodel`
--
ALTER TABLE `app2_portfoliomodel`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `app2_productsmodel`
--
ALTER TABLE `app2_productsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app2_productsmodel_portfolioModel_id_ffdaa226_fk_app2_port` (`portfolioModel_id`);

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
-- AUTO_INCREMENT cho bảng `app1_cartitemmodel`
--
ALTER TABLE `app1_cartitemmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app1_cartmodel`
--
ALTER TABLE `app1_cartmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app1_contactmodel`
--
ALTER TABLE `app1_contactmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app1_ordermodel`
--
ALTER TABLE `app1_ordermodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app1_postblog`
--
ALTER TABLE `app1_postblog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app1_usermodel`
--
ALTER TABLE `app1_usermodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `app2_portfoliomodel`
--
ALTER TABLE `app2_portfoliomodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `app2_productsmodel`
--
ALTER TABLE `app2_productsmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT cho bảng `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `app1_cartitemmodel`
--
ALTER TABLE `app1_cartitemmodel`
  ADD CONSTRAINT `app1_cartitemmodel_cart_id_c8389927_fk_app1_cartmodel_id` FOREIGN KEY (`cart_id`) REFERENCES `app1_cartmodel` (`id`),
  ADD CONSTRAINT `app1_cartitemmodel_products_id_2b50f5f3_fk_app2_productsmodel_id` FOREIGN KEY (`products_id`) REFERENCES `app2_productsmodel` (`id`);

--
-- Các ràng buộc cho bảng `app1_cartmodel`
--
ALTER TABLE `app1_cartmodel`
  ADD CONSTRAINT `app1_cartmodel_user_id_9bf23b63_fk_app1_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `app1_usermodel` (`id`);

--
-- Các ràng buộc cho bảng `app1_ordermodel`
--
ALTER TABLE `app1_ordermodel`
  ADD CONSTRAINT `app1_ordermodel_cart_id_63c474c4_fk_app1_cartmodel_id` FOREIGN KEY (`cart_id`) REFERENCES `app1_cartmodel` (`id`),
  ADD CONSTRAINT `app1_ordermodel_user_id_4ae29bdf_fk_app1_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `app1_usermodel` (`id`);

--
-- Các ràng buộc cho bảng `app2_productsmodel`
--
ALTER TABLE `app2_productsmodel`
  ADD CONSTRAINT `app2_productsmodel_portfolioModel_id_ffdaa226_fk_app2_port` FOREIGN KEY (`portfolioModel_id`) REFERENCES `app2_portfoliomodel` (`id`);

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
