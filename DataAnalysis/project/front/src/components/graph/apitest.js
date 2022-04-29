import React, { useState, useEffect } from "react";
import * as Api from '../../api';
import axios from "axios";

function Test1() {
  let [result, setResult] = useState("");
  // useEffect를 사용하지 않고 아래를 출력해보세요.
  console.log(result);

  // axios.get을 호출하고 result에 반환되는 데이터를 저장하세요.
  useEffect(() => {
    Api.get("food", )
      .then((response) => setResult(response.data.data));
  }, []);
  return (
    <div>
      <h4>React Axios로 HTTP GET 요청하기</h4>
      <div>
        {/* result를 이용해 출력 결과와 동일하게 출력하세요. */}
        Name: {result.first_name + " " + result.last_name} <br />
        Email: {result.email} <br />
      </div>
    </div>
  );
}


function Test({ _id }) {
  let [result, setResult] = useState([]);
  // useEffect를 사용하지 않고 아래를 출력해보세요.
  console.log(result);

  // axios.get을 호출하고 result에 반환되는 데이터를 저장하세요.
  useEffect(() => {
    Api.get("food", _id)
      .then((response) => setResult(response.data));
  }, [_id]);
  return (
    <div>
      <h4>React Axios로 HTTP GET 요청하기</h4>
      <div>
        {/* result를 이용해 출력 결과와 동일하게 출력하세요. */}
        Name: {result.first_name + " " + result.last_name} <br />
        Email: {result.email} <br />
      </div>
      <p></p>
    </div>
  );
}

//fetch 잘됨
function Test2_2() {
  fetch('http://localhost:5001/graph/1')
    .then(response => {
      return response.json()
    })
    .then(json => {
      console.log('body : ', json)
    })
  return (
    <div>
      <h2>featch TEST!!!</h2>
    </div>
  )
}

// 엘리스 잘됨
function Test2() {
  let [result, setResult] = useState("");
  // useEffect를 사용하지 않고 아래를 출력해보세요.
  console.log(result);

  // axios.get을 호출하고 result에 반환되는 데이터를 저장하세요.
  useEffect(() => {
    axios
      .get("https://reqres.in/api/users/2")
      .then((response) => setResult(response.data.data));
  }, []);
  return (
    <div>
      <h4>React Axios로 HTTP GET 요청하기</h4>
      <div>
        {/* result를 이용해 출력 결과와 동일하게 출력하세요. */}
        Name: {result.first_name + " " + result.last_name} <br />
        Email: {result.email} <br />
      </div>
    </div>
  );
}



export default Test2_2;



// 블로그
/* 
function Test3() {
  axios.get("https://reqres.in/api/users/2")
    .then(function (response) {
  
// 성공했을 때
      console.log(response);

})
    .catch(function (error) {
// 에러가 났을 때
      console.log(error);
})
    .finally(function () {
// 항상 실행되는 함수
      console.log('finally!!gogo');
    });
  return (
    <div>
      <h2>test####3333</h2>
      <p>ghghghghgh</p>
    </div>
  );

}
  const serverUrl =
  "https://reqres.in/api/users/";

  async function get(endpoint, params = "") {
    console.log(
      `%cGET 요청 ${serverUrl + endpoint + "/" + params}`,
      "color: #a25cd1;"
    );

    return axios.get(serverUrl + endpoint + "/" + params, {
      // JWT 토큰을 헤더에 담아 백엔드 서버에 보냄.
      headers: {
        Authorization: `Bearer ${sessionStorage.getItem("userToken")}`,
      },
    });
  }


const backendPortNumber = "5001";

function Test1(){
  const serverUrl =
  "https://reqres.in/api/users/";

  async function get(endpoint, params = "") {
    console.log(
      `%cGET 요청 ${serverUrl + endpoint + "/" + params}`,
      "color: #a25cd1;"
    );

    return axios.get(serverUrl + endpoint + "/" + params, {
      // JWT 토큰을 헤더에 담아 백엔드 서버에 보냄.
      headers: {
        Authorization: `Bearer ${sessionStorage.getItem("userToken")}`,
      },
    });
  }
  return (
    <div>
      <h2>test1test1</h2>
    </div>
  )
}


*/


