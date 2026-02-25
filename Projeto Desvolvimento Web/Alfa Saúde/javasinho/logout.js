const token = localStorage.getItem('access_token')

function logout(){
    localStorage.removeItem('access_token')
    window.location.href = "index.html";
}