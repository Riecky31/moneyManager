export interface Transaction {
  id: number
  amount: string
  category: number
  description?: string
  date: string
}

export interface TokenResponse {
  access: string
  refresh: string
}
