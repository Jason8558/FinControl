function add_transaction() {
    const form = document.querySelector("#transactions_form")
    const FD = new FormData(form)

    const JsonBody = {}
    FD.forEach((value, key) => {
        JsonBody[key] = value
    })

    urlwithoutslash = JsonBody['url'].split('/')[1]
    url =  document.URL + urlwithoutslash

    sendPostRequest(url, JsonBody)

    async function sendPostRequest(url, data) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // или 'application/x-www-form-urlencoded'
                    'X-CSRFToken': getCookie('csrftoken'), // для Django
                },
                body: JSON.stringify(data), // данные в формате JSON
            });
    
            if (!response.ok) {
                throw new Error(`Ошибка HTTP: ${response.status}`);
            }
    
            const result = await response.json(); // если сервер возвращает JSON
            console.log('Успешно:', result);
            return result;
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }


    function getCookie(name) {
        const cookies = document.cookie.split('; ');
        for (const cookie of cookies) {
          const [cookieName, cookieValue] = cookie.split('=');
          if (cookieName === name) {
            return decodeURIComponent(cookieValue);
          }
        }
        return null;
      }

}