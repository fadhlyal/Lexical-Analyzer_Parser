import streamlit as st
import time
import string

with st.sidebar:
    st.title('Lexical Analyzer & Parser')
    st.subheader('by Kelompok 4 (IF4411) \n'
                 '1. Fadhly Al-farizi (1301201472) \n 2. Fadli Zuhri (1301202613) \n 3. Kian Nailaizza (1301204455)')

st.title('Kata yang Bisa Diproses (Bahasa Arab)')
col1, col2 = st.columns(2)
with col1:
    st.warning('Kata Benda (Noun)')
    st.write('**1. durjun**')
    st.write('**2. abun**')
    st.write('**3. ummun**')
    st.write('**4. fulan**')
    st.write('**5. daftarun**')
    st.write('**6. tannuurotun**')
with col2:
    st.warning('Kata Kerja (Verb)')
    st.write('**1. dharaba**')
    st.write('**2. jaraha**')
    st.write('**3. kataba**')
    st.write('**4. darrasa**')
    
alphabet = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 
         'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 
         'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 
         'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31',
         'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39']

tabel_transisi = {}

for state in state_list :
    for huruf in alphabet :
        tabel_transisi[(state, huruf)] = 'error'
    tabel_transisi[(state, '#')] = 'error'
    tabel_transisi[(state, ' ')] = 'error'

tabel_transisi[('q0',' ')] = 'q0'

#fulan
tabel_transisi[('q0','f')] = 'q1'
tabel_transisi[('q1','u')] = 'q2'
tabel_transisi[('q2','l')] = 'q3'
tabel_transisi[('q3','a')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#abun
tabel_transisi[('q0','a')] = 'q4'
tabel_transisi[('q4','b')] = 'q35'
tabel_transisi[('q35','u')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#ummun
tabel_transisi[('q0','u')] = 'q5'
tabel_transisi[('q5','m')] = 'q6'
tabel_transisi[('q6','m')] = 'q35'
tabel_transisi[('q35','u')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#tannuurotun
tabel_transisi[('q0','t')] = 'q7'
tabel_transisi[('q7','a')] = 'q8'
tabel_transisi[('q8','n')] = 'q9'
tabel_transisi[('q9','n')] = 'q10'
tabel_transisi[('q10','u')] = 'q11'
tabel_transisi[('q11','u')] = 'q12'
tabel_transisi[('q12','r')] = 'q13'
tabel_transisi[('q13','o')] = 'q14'
tabel_transisi[('q14','t')] = 'q35'
tabel_transisi[('q35','u')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#durjun
tabel_transisi[('q0','d')] = 'q15'
tabel_transisi[('q15','u')] = 'q16'
tabel_transisi[('q16','r')] = 'q17'
tabel_transisi[('q17','j')] = 'q35'
tabel_transisi[('q35','u')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#daftarun
tabel_transisi[('q0','d')] = 'q15'
tabel_transisi[('q15','a')] = 'q18'
tabel_transisi[('q18','f')] = 'q19'
tabel_transisi[('q19','t')] = 'q20'
tabel_transisi[('q20','a')] = 'q21'
tabel_transisi[('q21','r')] = 'q35'
tabel_transisi[('q35','u')] = 'q36'
tabel_transisi[('q36','n')] = 'q38'
#darrasa
tabel_transisi[('q0','d')] = 'q15'
tabel_transisi[('q15','a')] = 'q18'
tabel_transisi[('q18','r')] = 'q22'
tabel_transisi[('q22','r')] = 'q23'
tabel_transisi[('q23','a')] = 'q24'
tabel_transisi[('q24','s')] = 'q37'
tabel_transisi[('q37','a')] = 'q38'
#dharaba
tabel_transisi[('q0','d')] = 'q15'
tabel_transisi[('q15','h')] = 'q25'
tabel_transisi[('q25','a')] = 'q26'
tabel_transisi[('q26','r')] = 'q27'
tabel_transisi[('q27','a')] = 'q28'
tabel_transisi[('q28','b')] = 'q37'
tabel_transisi[('q37','a')] = 'q38'
#kataba
tabel_transisi[('q0','k')] = 'q29'
tabel_transisi[('q29','a')] = 'q30'
tabel_transisi[('q30','t')] = 'q27'
tabel_transisi[('q27','a')] = 'q28'
tabel_transisi[('q28','b')] = 'q37'
tabel_transisi[('q37','a')] = 'q38'
#jaraha
tabel_transisi[('q0','j')] = 'q31'
tabel_transisi[('q31','a')] = 'q32'
tabel_transisi[('q32','r')] = 'q33'
tabel_transisi[('q33','a')] = 'q34'
tabel_transisi[('q34','h')] = 'q37'
tabel_transisi[('q37','a')] = 'q38'

#transisi token baru
tabel_transisi[('q39','f')] = 'q1'
tabel_transisi[('q39','a')] = 'q4'
tabel_transisi[('q39','u')] = 'q5'
tabel_transisi[('q39','t')] = 'q7'
tabel_transisi[('q39','d')] = 'q15'
tabel_transisi[('q39','k')] = 'q29'
tabel_transisi[('q39','j')] = 'q31'

#transisi accept token or spasi
tabel_transisi[('q38',' ')] = 'q39'
tabel_transisi[('q38','#')] = 'accept'
tabel_transisi[('q39',' ')] = 'q39'
tabel_transisi[('q39','#')] = 'accept'

with st.form(key='Form Input Kalimat'):
    kalimat = st.text_input('Kalimat')
    st.form_submit_button('Check')
#kalimat = ' durjun abun       ummun       fulan      daftarun tannuurotun dharaba jaraha kataba kataba'
kalimat_baru = kalimat.lower()+'#'
kalimat_temp = kalimat.split()

index_kalimat = 0
index_kata = 0
state = 'q0'
token = ''
while state != 'accept' :
    cari_huruf = kalimat_baru[index_kalimat]
    if cari_huruf != ' ':
        token = token + cari_huruf
    state = tabel_transisi[(state, cari_huruf)]
    index_kalimat = index_kalimat + 1
    if state == 'q38' and (kalimat_baru[index_kalimat] == ' ' or kalimat_baru[index_kalimat] == '#') :
        st.info('current token: '+token+', valid')
        token = ''
        index_kata = index_kata + 1
    if kalimat == '' :
        break;
    if state == 'error' :
        st.error('Kata **'+kalimat_temp[index_kata]+'** Tidak Valid')
        break;

if state == 'accept' :
    st.success('semua token di input: **'+kalimat+'**, valid')