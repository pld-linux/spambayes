Summary:	Spambayes - tool used to segregate unwanted mail
Summary(pl):	Spambayes - to narzêdzie do oddzielania niechcianej poczty
Name:		spambayes
Version:	1.0a6.1
Release:	0.1
License:	distributable
Group:		Applications/Mail
Vendor:		<spambayes@python.org>
Source0:	http://dl.sourceforge.net/spambayes/%{name}-%{version}.tar.gz
# Source0-md5:	f8b84ef6b582334794eaf97718b5ad9f
Patch0:		%{name}-doc_paths.patch
Patch1:		%{name}-scripts.patch
URL:		http://spambayes.sourceforge.net/
BuildRequires:	ed
Requires:	rpm-pythonprov
Requires:	python >= 2.2
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
%setup -q -n %{name}-1.0a6
%patch0 -p1
%patch1 -p1

%build
chmod 644 utilities/loosecksum.py
echo -e ",s:/usr/local/bin/python:/usr/bin/python:g\n,w\nq" | ed utilities/loosecksum.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/spambayes,/tmp/{contrib,pspam}}

install *.py $RPM_BUILD_ROOT%{_libdir}/spambayes
cp -r contrib pspam spambayes testtools utilities $RPM_BUILD_ROOT%{_libdir}/spambayes

install contrib/BULK.txt $RPM_BUILD_ROOT/tmp/contrib
install pspam/README.txt $RPM_BUILD_ROOT/tmp/pspam

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%doc $RPM_BUILD_ROOT/tmp/{pspam,contrib}
%dir %{_libdir}/spambayes
%attr(755,root,root) %{_libdir}/spambayes/*.py
%dir %{_libdir}/spambayes/contrib
%attr(755,root,root) %{_libdir}/spambayes/contrib/b*
%{_libdir}/spambayes/contrib/[Smps]*
%dir %{_libdir}/spambayes/pspam
%attr(755,root,root) %{_libdir}/spambayes/pspam/[sz]*
%{_libdir}/spambayes/pspam/[puv]*
%dir %{_libdir}/spambayes/spambayes
%attr(755,root,root) %{_libdir}/spambayes/spambayes/[FHhst]*
%attr(755,root,root) %{_libdir}/spambayes/spambayes/Corpus.py
%attr(755,root,root) %{_libdir}/spambayes/spambayes/cdb.py
%attr(755,root,root) %{_libdir}/spambayes/spambayes/classifier.py
%attr(755,root,root) %{_libdir}/spambayes/spambayes/mboxutils.py
%attr(755,root,root) %{_libdir}/spambayes/spambayes/message.py
%{_libdir}/spambayes/spambayes/[_DOPTdor]*
%{_libdir}/spambayes/spambayes/CostCounter.py
%{_libdir}/spambayes/spambayes/ImapUI.py
%{_libdir}/spambayes/spambayes/UserInterface.py
%{_libdir}/spambayes/spambayes/Version.py
%{_libdir}/spambayes/spambayes/c[ho]*
%{_libdir}/spambayes/spambayes/cdb_*
%{_libdir}/spambayes/spambayes/msgs.py
%dir %{_libdir}/spambayes/testtools
%attr(755,root,root) %{_libdir}/spambayes/testtools/[!s]*
%{_libdir}/spambayes/testtools/s*
%attr(755,root,root) %{_libdir}/spambayes/utilities
