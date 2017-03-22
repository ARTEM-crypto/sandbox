(ns clojure-noob.core
  (:gen-class))

   
(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "I'm a little teapot!"))


(def asym-hobbit-body-parts [{:name "head" :size 3}
                             {:name "left-eye" :size 1}
                             {:name "left-ear" :size 1}
                             {:name "mouth" :size 1}
                             {:name "nose" :size 1}
                             {:name "neck" :size 2}
                             {:name "left-shoulder" :size 3}
                             {:name "left-upper-arm" :size 3}
                             {:name "chest" :size 10}
                             {:name "back" :size 10}
                             {:name "left-forearm" :size 3}
                             {:name "abdomen" :size 6}
                             {:name "left-kidney" :size 1}
                             {:name "left-hand" :size 2}
                             {:name "left-knee" :size 2}
                             {:name "left-thigh" :size 4}
                             {:name "left-lower-leg" :size 3}
                             {:name "left-achilles" :size 1}
                             {:name "left-foot" :size 2}])

(def asym-alien-body-parts [{:name "head" :size 3}
                             {:name "1-eye" :size 1}
                             {:name "1-ear" :size 1}
                             {:name "mouth" :size 1}
                             {:name "nose" :size 1}
                             {:name "neck" :size 2}
                             {:name "1-shoulder" :size 3}
                             {:name "1-upper-arm" :size 3}
                             {:name "chest" :size 10}
                             {:name "back" :size 10}
                             {:name "1-forearm" :size 3}
                             {:name "abdomen" :size 6}
                             {:name "1-kidney" :size 1}
                             {:name "1-hand" :size 2}
                             {:name "1-knee" :size 2}
                             {:name "1-thigh" :size 4}
                             {:name "1-lower-leg" :size 3}
                             {:name "1-achilles" :size 1}
                             {:name "1-foot" :size 2}])

(defn matching-part
  [part]
  {:name (clojure.string/replace (:name part) #"^left-" "right-")
   :size (:size part)})

(defn symmetrize-body-parts
  [asym-body-parts]
  (loop [remaining-asym-parts asym-body-parts
         final-body-parts []]
    (if (empty? remaining-asym-parts)
      final-body-parts
      (let [[part & remaining] remaining-asym-parts]
        (recur remaining 
               (into final-body-parts 
                     (set [part (matching-part part)])))))))


(defn better-symmetrize-body-parts
  [asym-body-parts]
  (reduce (fn [final-body-parts part]
            (into final-body-parts (set [part (matching-part part)])))
          []
          asym-body-parts))

(defn matching-parts
  [part]
  (if (re-find #"^1-" (:name part))
    (let [name-last-index (count (:name part))]
      (loop [number 2
             final-parts [part]]
        (if (< (count final-parts) 5)
           (recur (inc number)
                  (conj final-parts 
                    {:name (str number (subs (:name part) 1 name-last-index))
                     :size (:size part)}))
          final-parts)))
    [part]))

(defn add-alien-body-parts
  [alien-body-parts]
  (reduce (fn [final-body-parts part]
            (into final-body-parts (set (into [part] (matching-parts part)))))
          []
          alien-body-parts))

(defn dec-maker
  [number]
  #(- % number))

(defn mapset
  [f coll]
  (let [collset (set coll)]
    (map f collset)))
