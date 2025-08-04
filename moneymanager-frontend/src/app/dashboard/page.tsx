'use client'

import { useEffect, useState } from 'react'
import api from '@/lib/api'
import { Transaction } from '@/types'
import { useRouter } from 'next/navigation'

export default function Dashboard() {
  const [transactions, setTransactions] = useState<Transaction[]>([])
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('access')
    if (!token) {
      router.push('/login')
      return
    }

    api
      .get<Transaction[]>('transactions/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => setTransactions(res.data))
      .catch(() => {
        router.push('/login')
      })
  }, [router])

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Transactions</h1>
      <ul className="space-y-2">
        {transactions.map((t) => (
          <li key={t.id} className="p-4 bg-white rounded shadow">
            ID {t.id}: Category {t.category} — ${t.amount}
          </li>
        ))}
      </ul>
    </div>
  )
}
