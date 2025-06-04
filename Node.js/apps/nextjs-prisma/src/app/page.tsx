'use client'
// import { signIn, signOut, useSession } from 'next-auth/react'

export default function Home() {
  // const { data: session } = useSession()
  // console.log(11111, session)
  return 1
  return (
    <>
      {/* {session ? ( */}
      <>
        {/* <p>欢迎, {session.user?.name}</p> */}
        {/* <button onClick={() => signOut()}>退出</button> */}
      </>
      {/* ) : ( */}
      <>
        {/* <p>请登录</p> */}
        {/* <button onClick={() => signIn('github')}>使用 GitHub 登录</button> */}
      </>
      {/* )} */}
    </>
  )
}
