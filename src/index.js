import React, {useState, useEffect, useCallback} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Stock from './stock'
import Navbar from './navbar'
import Popup from './popup'
import {useFetch} from './useFetch'
import axios from 'axios'


function App() {
  const [show, setShow] = useState(false)
  const [firstName, setFirstName] = useState('');
  const [email, setEmail] = useState('');
  const [person, setPerson] = useState({});

  const url = 'http://127.0.0.1:8000/api/'
  const {loading, stocks} = useFetch(url)

  const handleSubmit = (e) => {
    e.preventDefault();
    if (firstName && email) {
      const p = { id: new Date().getTime().toString(), firstName, email }
          axios.post('http://127.0.0.1:8000/api/signup', {
            first_name: p.firstName,
            email: p.email,
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
          setFirstName('');
          setEmail('');
          setPerson({})
          setShow(false)
        } else {
          console.log('empty values');
        }
      };
  if(!show){
    return (
    <div className="card">
      <button type="button" onClick={()=>setShow(true)} className="btn" style={{'margin':'2rem', 'display':'inline', 'textAlign':'right'}}>Join</button>
      {loading ? 'loading...' : <Stock stock={stocks[0]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[1]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[2]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[3]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[4]}/>}
    </div>
    );

  } else{
    return (
    <>
    <div className="bg">
      <div className="modal">
        <button type="button" id="close-btn" className="close-btn" onClick={()=>{
          setShow(false)
        }}>+</button>
        <br/><br/>
        <h3 style={{'textAlign':'center'}}>Recieve Updates</h3>
        <br/>
        <div className="p-container">
        <p style={{'textAlign':'center'}}>
          Fill out your information below and we will send you information on the best stocks to buy every week
        </p>
        </div>
        <br></br>
        <hr />
        <form className='form' onSubmit={handleSubmit}>
          <div className='form-control'>
            <label htmlFor='firstName'>Name : </label>
            <input
              type='text'
              id='firstName'
              name='firstName'
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
          </div>
          <div className='form-control'>
            <label htmlFor='email'>Email : </label>
            <input
              type='email'
              id='email'
              name='email'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <button type='submit' className="btn">submit</button>
        </form>
      </div>
    </div>

    <div className="card">
      <button onClick={()=>setShow(true)} className="btn" style={{'margin':'2rem', 'display':'inline', 'textAlign':'right'}}>Join</button>
      {loading ? 'loading...' : <Stock stock={stocks[0]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[1]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[2]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[3]}/>}
      {loading ? 'loading...' : <Stock stock={stocks[4]}/>}
    </div>
    </>
  );
  }
}


ReactDOM.render(
  <React.StrictMode>
    <Navbar/>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

