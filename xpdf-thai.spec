Summary:	TIS-620 encoding support for xpdf
Summary(pl.UTF-8):	Wsparcie kodowania TIS-620 dla xpdf
Name:		xpdf-thai
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
# Source0-md5:	96e058c1b0429ae1ba0b50f1784b0985
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.)
This package provides support files needed to use the Xpdf tools with
Thai PDF files.

%description -l pl.UTF-8
Pakiety wspierające języki Xpdf zawierają pliki CMap, kodowania oraz
różne inne informacje konfiguracyjne niezbędne bądź przydatne przy
określonych zestawach znaków. (Nie zawierają żadnych fontów).
Ten pakiet zawiera pliki potrzebne do używania narzędzi Xpdf z
tajskimi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf
install *.nameToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	TIS-620	/usr/share/xpdf/TIS-620.unicodeMap' >> /etc/xpdfrc
	echo 'nameToUnicode		/usr/share/xpdf/Thai.nameToUnicode' >> /etc/xpdfrc
else
 if ! grep -q 'TIS-620\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	TIS-620	/usr/share/xpdf/TIS-620.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Thai\.nameToUnicode' /etc/xpdfrc; then
	echo 'nameToUnicode		/usr/share/xpdf/Thai.nameToUnicode' >> /etc/xpdfrc
 fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v 'TIS-620\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'Thai\.nameToUnicode' /etc/xpdfrc.new > /etc/xpdfrc
	rm -f /etc/xpdfrc.new
fi

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
