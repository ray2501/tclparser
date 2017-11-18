%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tclparser
Summary:       TclPro parser compoment
Version:       1.8
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        tclparser.tar.gz
URL:           https://github.com/flightaware/TclProDebug/tree/master/lib/tclparser
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.1
Requires:      tcl >= 8.1
BuildRoot:     %{buildroot}

%description
This is the Tcl parser component used by the checker to
parse a Tcl script into commands, words and tokens.

%prep
%setup -q -n %{name}

%build
CFLAGS="%optflags" ./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
