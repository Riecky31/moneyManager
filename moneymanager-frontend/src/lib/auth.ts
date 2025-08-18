import api from "./api";

export interface TokenResponse {
    access: string;
    refresh: string;
}

export async function login(username: string, password: string): Promise<void> {
    const res = await api.post <TokenResponse>("/token/", { username, password });
    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
}
export function logout(): void {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
}