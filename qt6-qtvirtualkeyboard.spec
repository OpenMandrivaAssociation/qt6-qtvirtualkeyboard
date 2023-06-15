%define beta beta1

Name:		qt6-qtvirtualkeyboard
Version:	6.6.0
Release:	%{?beta:0.%{beta}.1}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtvirtualkeyboard.git
Source:		qtvirtualkeyboard-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtvirtualkeyboard-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{qtmajor} virtual keyboard Library
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	qt6-cmake
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(OpenGL)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(hunspell)
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{qtmajor} virtual keyboard library

%global extra_files_VirtualKeyboard \
%{_qtdir}/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so \
%{_qtdir}/qml/QtQuick/VirtualKeyboard

%global extra_devel_files_VirtualKeyboard \
%{_qtdir}/lib/cmake/Qt6/FindCerenceHwrAlphabetic.cmake \
%{_qtdir}/lib/cmake/Qt6/FindCerenceHwrCjk.cmake \
%{_qtdir}/lib/cmake/Qt6/FindCerenceXt9.cmake \
%{_qtdir}/lib/cmake/Qt6/FindHunspell.cmake \
%{_qtdir}/lib/cmake/Qt6/FindMyScript.cmake \
%{_qtdir}/lib/cmake/Qt6BundledOpenwnn \
%{_qtdir}/lib/cmake/Qt6BundledPinyin \
%{_qtdir}/lib/cmake/Qt6BundledTcime \
%{_qtdir}/lib/cmake/Qt6Gui/Qt6QVirtualKeyboardPlugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylesplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentsplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutsplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbplugin[A-Z]*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginsplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingsplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylesplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimeplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaiplugin*.cmake

%global extra_devel_files_HunspellInputMethod \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellplugin*.cmake

%qt6libs VirtualKeyboard HunspellInputMethod

%package examples
Summary: Examples for the Qt %{major} Virtual Keyboard module
Group: Development/KDE and Qt

%description examples
Examples for the Qt %{major} Virtual Keyboard module

%files examples
%optional %{_qtdir}/examples/virtualkeyboard

%prep
%autosetup -p1 -n qtvirtualkeyboard%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_MKSPECS_DIR:FILEPATH=%{_qtdir}/mkspecs \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall
