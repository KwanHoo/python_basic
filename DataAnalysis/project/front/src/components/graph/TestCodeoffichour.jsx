import React from 'react'

const TestCodeoffichour = () => {
  return (
      <div>TestCodeoffichour

          {/* 온클릭 예시 코드 */}
          <div>
              <div>
                  {graphs.map((blog) => (
                      <div onClick={ }></div>
                  ))}
              </div>
          </div>

          {/* props로 컴포넌트 온클릭 전달1*/}
          <div>
              const GraphComponent =({onClick}) => {
                  <div onClick={onclick}>그래프컴포넌트</div>
              };

              function GraphMiddleArticle(graphs) {
                  return (
                    <div >
                  <div>
                      {graph.map((graph) => (
                          <GraphComponent onClick={} />
                      ))}
                        </div>
                    </div>
                  )
              }

              
                {/* props로 컴포넌트 온클릭 전달2*/}
                <div>
                    const GraphComponent =({onClick}) => {
                        <div onClick={onclick}>그래프 컴포넌트</div>
                    };

                    function GraphMiddleArticle(graphs) {
                        const navigate = useNavigate();
                        return (
                            <div >
                                <div>
                                    {graph.map((graph) => (
                                        <GraphComponent onClick={() => {
                                            navigate(`/graph/${graph.id}`);
                                        }} />
                                    ))}
                                </div>
                            </div>
                        )
                    }
              </div>

                  
                            {/* 예시1 */}

                  <div>
                      const LogoPart = () => {
                        const [data, setData] = useState();
                        useEffect(() => {
                            fetchData().then((d) => {
                                setData(data);
                            })
                        }, []);
                      return (
                      <div>
                          <div className='logo'>
                              <img src={Logo} alt="" />
                              
                          </div>
                        </div>
                        )

                    }
              </div>

                {/* 예시2 */}
                <div>
                      const LogoPart = () => {
                        const [data, setData] = useState();
                        useEffect(() => {
                            fetchData().then((d) => {
                                setData(data);
                            })
                  }, []);
                  useEffect(()=> {
                      //data 가공
                  },[data])
                      return (
                      <div>
                          <div className='logo'>
                              <img src={Logo} alt="" />
                              
                          </div>
                        </div>
                        )

                    }
              </div>
              
              
                


          </div>
    </div>
  )
}

export default TestCodeoffichour

