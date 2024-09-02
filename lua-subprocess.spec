%define luarocks_pkg_name subprocess
%define luarocks_pkg_version 0.5.6-14
%define luarocks_pkg_prefix subprocess-0.5.6-14
%define luarocks_pkg_major 0.5.6
%define luarocks_pkg_minor 14

Name: lua-subprocess
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Subprocess module for Lua
Url: https://github.com/huakim/lua-subprocess
License: LGPL
Source0: subprocess-0.5.6-14.tar.gz
Source1: subprocess-0.5.6-14.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
Requires: %{luadist lua >= 5.1}
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b
%endif

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
