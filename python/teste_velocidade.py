import streamlit as st
import speedtest_cli as sp

def main():
    st.header("SpeedTest", divider=True)
    st.write('Clique no botão a baixo para iniciar o teste')
    
    if st.button('Iniciar'):
        with st.spinner('Testando a velociadade da sua internet...'):
            s = sp.Speedtest()
            s.get_best_server()
            download_speed = s.download() / 1_000_000
            upload_speed = s.upload() / 1_000_000
            results = s.results.dict()
        
            max_speed = 100
            st.write(f"Velocidade de Download {download_speed:.2f} Mpbs")
            st.progress(min(download_speed / max_speed, 1.0))
        
            st.write(f"Velocidade de Upload {upload_speed:.2f} Mpbs")
            st.progress(min(upload_speed / max_speed, 1.0))
        
            st.write(f"Ping: {results['ping']} ms")

main()