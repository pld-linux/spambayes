%include	/usr/lib/rpm/macros.python
Summary:	Spambayes - tool used to segregate unwanted mail
Summary(pl):	Spambayes - narzêdzie do oddzielania niechcianej poczty
Name:		spambayes
Version:	1.0a9
Release:	1
License:	PSF
Group:		Applications/Mail
Vendor:		<spambayes@python.org>
Source0:	http://dl.sourceforge.net/spambayes/%{name}-%{version}.tar.gz
# Source0-md5:	90a6c190c9696d8be86eb027a778ebf7
Patch0:		%{name}-scripts.patch
URL:		http://spambayes.sourceforge.net/
BuildRequires:	ed
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spambayes is a tool used to segregate unwanted mail (spam) from the
mail you want (ham). Before Spambayes can be your spam filter of
choice you need to train it on representative samples of email you
receive. After it's been trained, you use Spambayes to classify new
mail according to its spamminess and hamminess qualities.

%description -l pl
Spambayes jest narzêdziem s³u¿±cym do oddzielania niechcianej poczty
(spamu) od poczty po¿±danej (ham). Zanim Spambayes stanie siê filtrem
spamu o po¿±danych przez u¿ytkownika cechach, trzeba go nauczyæ na
podstawie reprezentatywnych próbek otrzymanej poczty. Po nauczeniu,
mo¿na u¿ywaæ Spambayesa do klasyfikowania nowej poczty w zale¿no¶ci od
stopnia jej "spamowo¶ci".

%prep
%setup -q
# Files in the tarball are 0444, so patching will not
# work without this.
chmod -R u+w .
%patch0 -p1

echo -e ",s:/usr/local/bin/python:/usr/bin/python:g\n,w\nq" | ed utilities/loosecksum.py

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
