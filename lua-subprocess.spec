%define luarocks_pkg_name subprocess
%define luarocks_pkg_version 0.5.5-1
%define luarocks_pkg_prefix subprocess-0.5.5-1
%define luarocks_pkg_major 0.5.5
%define luarocks_pkg_minor 1
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true

Name: lua-subprocess
BuildRequires: lua-rpm-macros

%if %{defined luarocks_requires}
%luarocks_requires
%else
BuildRequires: %{lua_module luarocks}
BuildRequires: %{lua_module devel}
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: make
%endif
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Subprocess module for Lua
Url: https://github.com/huakim/lua-subprocess
License: LGPL
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
Requires: %{luadist lua >= 5.1}

Source0: subprocess-0.5.5-1.tar.gz
Source1: subprocess-0.5.5-1.rockspec
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  

%prep
%autosetup -p1 -n %luarocks_pkg_prefix
%luarocks_prep

%generate_buildrequires

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}
%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}