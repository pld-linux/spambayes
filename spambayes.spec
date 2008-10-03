Summary:	Spambayes - tool used to segregate unwanted mail
Summary(pl.UTF-8):	Spambayes - narzędzie do oddzielania niechcianej poczty
Name:		spambayes
Version:	1.0.4
Release:	2
Epoch:		1
License:	PSF
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/spambayes/%{name}-%{version}.tar.gz
# Source0-md5:	78c33e79888d410711ff3c7dd7e98d79
URL:		http://spambayes.sourceforge.net/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.140
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spambayes is a tool used to segregate unwanted mail (spam) from the
mail you want (ham). Before Spambayes can be your spam filter of
choice you need to train it on representative samples of email you
receive. After it's been trained, you use Spambayes to classify new
mail according to its spamminess and hamminess qualities.

%description -l pl.UTF-8
Spambayes jest narzędziem służącym do oddzielania niechcianej poczty
(spamu) od poczty pożądanej (ham). Zanim Spambayes stanie się filtrem
spamu o pożądanych przez użytkownika cechach, trzeba go nauczyć na
podstawie reprezentatywnych próbek otrzymanej poczty. Po nauczeniu,
można używać Spambayesa do klasyfikowania nowej poczty w zależności od
stopnia jej "spamowości".

%prep
%setup -q
%{__sed} -i -e '1s,#!.*/bin/python,#!%{_bindir}/python,' utilities/loosecksum.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

#install -d $RPM_BUILD_ROOT{%{_libdir}/spambayes,/tmp/{contrib,pspam}}
#cp -r contrib pspam spambayes testtools utilities $RPM_BUILD_ROOT%{_libdir}/spambayes
#install contrib/BULK.txt $RPM_BUILD_ROOT/tmp/contrib
#install pspam/README.txt $RPM_BUILD_ROOT/tmp/pspam

find $RPM_BUILD_ROOT%{py_sitescriptdir}/spambayes -name '*.py' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/sb_*.py
%{py_sitescriptdir}/spambayes
